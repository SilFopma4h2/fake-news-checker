"""
Tests for 3D Model Viewer Platform
Simple tests to verify core functionality
"""
import sys
import os
import tempfile
import io

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_db, add_model, get_model, get_all_models, delete_model
from app import app, allowed_file

def test_database_operations():
    """Test database CRUD operations"""
    print("Testing database operations...")
    
    # Test database initialization
    if os.path.exists('models.db'):
        os.remove('models.db')
    
    init_db()
    assert os.path.exists('models.db'), "Database file should be created"
    print("✓ Database initialization works")
    
    # Test adding model
    model_id = add_model(
        filename='test123.glb',
        original_filename='test_model.glb',
        file_path='uploads/test123.glb'
    )
    assert model_id > 0, "Model ID should be positive"
    print(f"✓ Adding model works (ID: {model_id})")
    
    # Test getting model
    model = get_model(model_id)
    assert model is not None, "Model should exist"
    assert model['filename'] == 'test123.glb', "Filename should match"
    assert model['original_filename'] == 'test_model.glb', "Original filename should match"
    print("✓ Getting model works")
    
    # Test getting all models
    models = get_all_models()
    assert len(models) == 1, "Should have 1 model"
    print("✓ Getting all models works")
    
    # Test deleting model
    deleted = delete_model(model_id)
    assert deleted, "Model should be deleted"
    model = get_model(model_id)
    assert model is None, "Model should not exist after deletion"
    print("✓ Deleting model works")
    
    # Cleanup
    os.remove('models.db')
    
    print("✅ All database tests passed!\n")

def test_file_validation():
    """Test file validation function"""
    print("Testing file validation...")
    
    # Test valid files
    assert allowed_file('model.glb'), "GLB files should be allowed"
    assert allowed_file('scene.gltf'), "GLTF files should be allowed"
    assert allowed_file('MODEL.GLB'), "Uppercase extensions should work"
    print("✓ Valid file extensions accepted")
    
    # Test invalid files
    assert not allowed_file('image.jpg'), "JPG files should not be allowed"
    assert not allowed_file('document.pdf'), "PDF files should not be allowed"
    assert not allowed_file('script.py'), "Python files should not be allowed"
    assert not allowed_file('noextension'), "Files without extension should not be allowed"
    print("✓ Invalid file extensions rejected")
    
    print("✅ All file validation tests passed!\n")

def test_flask_routes():
    """Test Flask application routes"""
    print("Testing Flask routes...")
    
    # Setup - ensure database exists
    if os.path.exists('models.db'):
        os.remove('models.db')
    init_db()
    
    app.config['TESTING'] = True
    client = app.test_client()
    
    # Test home page
    response = client.get('/')
    assert response.status_code == 200, "Home page should return 200"
    assert b'3D Model Viewer' in response.data or b'Upload' in response.data, "Home page should contain relevant content"
    print("✓ Home page loads successfully")
    
    # Test models list page
    response = client.get('/models')
    assert response.status_code == 200, "Models page should return 200"
    print("✓ Models list page loads successfully")
    
    # Test invalid model view
    response = client.get('/view/99999')
    assert response.status_code == 404, "Non-existent model should return 404"
    print("✓ Invalid model returns 404")
    
    # Test upload endpoint without file
    response = client.post('/upload')
    assert response.status_code == 400, "Upload without file should return 400"
    print("✓ Upload validation works")
    
    # Cleanup
    if os.path.exists('models.db'):
        os.remove('models.db')
    
    print("✅ All Flask route tests passed!\n")

def test_upload_flow():
    """Test complete upload flow"""
    print("Testing upload flow...")
    
    # Setup
    if os.path.exists('models.db'):
        os.remove('models.db')
    init_db()
    
    os.makedirs('uploads', exist_ok=True)
    
    app.config['TESTING'] = True
    client = app.test_client()
    
    # Create a fake GLB file
    fake_file = io.BytesIO(b'fake glb content for testing')
    fake_file.name = 'test.glb'
    
    # Test upload
    response = client.post('/upload', data={
        'model': (fake_file, 'test.glb')
    }, content_type='multipart/form-data')
    
    assert response.status_code == 200, "Upload should succeed"
    data = response.get_json()
    assert 'model_id' in data, "Response should contain model_id"
    assert 'view_url' in data, "Response should contain view_url"
    print(f"✓ Upload successful (Model ID: {data['model_id']})")
    
    # Test viewing uploaded model
    model_id = data['model_id']
    response = client.get(f'/view/{model_id}')
    assert response.status_code == 200, "View page should load"
    print("✓ View page loads for uploaded model")
    
    # Cleanup
    models = get_all_models()
    for model in models:
        if os.path.exists(model['file_path']):
            os.remove(model['file_path'])
    
    if os.path.exists('models.db'):
        os.remove('models.db')
    
    print("✅ All upload flow tests passed!\n")

if __name__ == "__main__":
    print("=" * 60)
    print("3D Model Viewer Platform - Component Tests")
    print("=" * 60)
    print()
    
    try:
        test_database_operations()
        test_file_validation()
        test_flask_routes()
        test_upload_flow()
        
        print("=" * 60)
        print("✅ All tests completed successfully!")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
