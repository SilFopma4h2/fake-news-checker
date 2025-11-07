"""
3D Model Viewer Platform
A web application for uploading, viewing, and sharing 3D models
Built with Flask, Three.js, and SQLite
"""
from flask import Flask, render_template, request, jsonify, send_from_directory, redirect, url_for
import os
from werkzeug.utils import secure_filename
from database import init_db, add_model, get_model, get_all_models
import uuid

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'glb', 'gltf'}
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize database
init_db()

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Main page with upload form"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle 3D model file upload"""
    try:
        # Check if file is in request
        if 'model' not in request.files:
            return jsonify({'error': 'Geen bestand gevonden'}), 400
        
        file = request.files['model']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({'error': 'Geen bestand geselecteerd'}), 400
        
        # Check if file extension is allowed
        if not allowed_file(file.filename):
            return jsonify({'error': 'Alleen .glb en .gltf bestanden zijn toegestaan'}), 400
        
        # Generate unique filename
        original_filename = secure_filename(file.filename)
        file_extension = original_filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{uuid.uuid4().hex}.{file_extension}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        
        # Save file
        file.save(file_path)
        
        # Add to database
        model_id = add_model(
            filename=unique_filename,
            original_filename=original_filename,
            file_path=file_path
        )
        
        return jsonify({
            'success': True,
            'model_id': model_id,
            'message': 'Model succesvol geüpload',
            'view_url': f'/view/{model_id}'
        })
        
    except Exception as e:
        return jsonify({'error': f'Upload fout: {str(e)}'}), 500

@app.route('/view/<int:model_id>')
def view_model(model_id):
    """View a specific 3D model"""
    model = get_model(model_id)
    
    if not model:
        return "Model niet gevonden", 404
    
    return render_template('viewer.html', model=model)

@app.route('/models/<int:model_id>')
def get_model_info(model_id):
    """API endpoint to get model information"""
    model = get_model(model_id)
    
    if not model:
        return jsonify({'error': 'Model niet gevonden'}), 404
    
    return jsonify(model)

@app.route('/uploads/<path:filename>')
def serve_model(filename):
    """Serve uploaded model files"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/models')
def list_models():
    """List all uploaded models"""
    models = get_all_models()
    return render_template('models.html', models=models)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
