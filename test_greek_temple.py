"""
Test script for Greek Temple 3D model
Verifies the generated GLB file is valid and can be loaded
"""
import os
import trimesh
from pathlib import Path


def test_greek_temple_file():
    """Test that the Greek temple GLB file exists and is valid."""
    print("Testing Greek Temple GLB file...")
    
    # Check file exists
    temple_path = Path("uploads/greek_temple.glb")
    assert temple_path.exists(), f"Greek temple file not found at {temple_path}"
    print(f"✓ File exists: {temple_path}")
    
    # Check file size
    file_size = temple_path.stat().st_size
    assert file_size > 0, "File is empty"
    print(f"✓ File size: {file_size / 1024:.2f} KB")
    
    # Try to load the mesh
    try:
        loaded = trimesh.load(str(temple_path))
        print(f"✓ File loaded successfully")
        
        # Handle Scene objects (GLB files may be loaded as scenes)
        if isinstance(loaded, trimesh.Scene):
            # Extract the first geometry from the scene
            temple = loaded.to_geometry()
        else:
            temple = loaded
        
        # Verify it's a valid mesh
        assert hasattr(temple, 'vertices'), "No vertices in mesh"
        assert hasattr(temple, 'faces'), "No faces in mesh"
        assert len(temple.vertices) > 0, "No vertices"
        assert len(temple.faces) > 0, "No faces"
        
        print(f"✓ Mesh structure valid")
        print(f"  - Vertices: {len(temple.vertices)}")
        print(f"  - Faces: {len(temple.faces)}")
        print(f"  - Bounds: X:{temple.bounds[0][0]:.1f} to {temple.bounds[1][0]:.1f}, "
              f"Y:{temple.bounds[0][1]:.1f} to {temple.bounds[1][1]:.1f}, "
              f"Z:{temple.bounds[0][2]:.1f} to {temple.bounds[1][2]:.1f}")
        
        # Check if it's watertight (closed mesh)
        if temple.is_watertight:
            print(f"✓ Mesh is watertight (closed)")
        else:
            print(f"⚠ Mesh is not watertight (has holes) - this is OK for architectural models")
        
    except Exception as e:
        raise AssertionError(f"Failed to load mesh: {e}")
    
    print("\n✅ All tests passed! Greek temple model is valid.\n")


def test_model_features():
    """Test that the Greek temple has expected architectural features."""
    print("Testing architectural features...")
    
    loaded = trimesh.load("uploads/greek_temple.glb")
    
    # Handle Scene objects
    if isinstance(loaded, trimesh.Scene):
        temple = loaded.to_geometry()
    else:
        temple = loaded
    
    # Check that model has reasonable dimensions (not too small or huge)
    bounds = temple.bounds
    width = bounds[1][0] - bounds[0][0]
    depth = bounds[1][1] - bounds[0][1]
    height = bounds[1][2] - bounds[0][2]
    
    assert 10 < width < 30, f"Width {width} seems incorrect"
    assert 5 < depth < 20, f"Depth {depth} seems incorrect"
    assert 5 < height < 20, f"Height {height} seems incorrect"
    
    print(f"✓ Dimensions are reasonable:")
    print(f"  - Width: {width:.1f}")
    print(f"  - Depth: {depth:.1f}")
    print(f"  - Height: {height:.1f}")
    
    # Check vertex count is reasonable for a temple
    assert 1000 < len(temple.vertices) < 10000, "Vertex count seems wrong"
    print(f"✓ Vertex count is appropriate: {len(temple.vertices)}")
    
    # Check that model sits on or above ground (Z >= 0)
    min_z = temple.bounds[0][2]
    assert min_z >= -0.1, f"Model extends below ground: {min_z}"
    print(f"✓ Model sits on ground (min Z: {min_z:.2f})")
    
    print("\n✅ All architectural features validated!\n")


if __name__ == "__main__":
    print("=" * 60)
    print("Greek Temple 3D Model Tests")
    print("=" * 60)
    print()
    
    try:
        test_greek_temple_file()
        test_model_features()
        
        print("=" * 60)
        print("✅ All tests completed successfully!")
        print("=" * 60)
        print("\nThe Greek temple is ready to be viewed in the 3D Model Viewer!")
        print("To view it, you can either:")
        print("1. Start the Flask app: python3 app.py")
        print("2. Navigate to http://localhost:5001")
        print("3. Upload the file: uploads/greek_temple.glb")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
