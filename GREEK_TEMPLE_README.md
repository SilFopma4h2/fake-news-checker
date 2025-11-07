# Greek Temple 3D Model Generator

This project includes a Python script that generates a clean, architecturally accurate 3D model of a Greek temple in GLB format.

## Features

The generated Greek temple includes:

- **Three-tiered platform (Stylobate)**: The characteristic raised base of Greek temples
- **Doric columns**: Classical columns with proper proportions arranged in a peristyle (surrounding colonnade)
  - 6 columns on the front and back
  - 4 additional columns on each side
  - Column capitals (tops) and bases
- **Entablature**: The horizontal structure resting on the columns
- **Pediment roof**: Triangular gable ends typical of Greek temple architecture
- **Cella**: The inner chamber/room of the temple
- **Clean geometric design**: Marble-like white appearance

## Requirements

Install the required dependencies:

```bash
pip install trimesh numpy pygltflib
```

These packages are used for:
- `trimesh`: 3D mesh creation and manipulation
- `numpy`: Mathematical operations for 3D geometry
- `pygltflib`: Exporting to GLB format

## Usage

### Generate the Temple

Run the generator script:

```bash
python3 generate_greek_temple.py
```

This will:
1. Create a 3D model of a Greek temple
2. Save it as `uploads/greek_temple.glb`
3. Display statistics about the generated model

### Output

The script generates a GLB file with the following characteristics:
- **Format**: GLB (binary glTF 2.0)
- **File size**: ~95 KB
- **Vertices**: ~2,460
- **Faces**: ~4,688
- **Dimensions**: 21 x 13 x 11.5 units (Width x Depth x Height)
- **Color**: Light marble-like white (RGB: 240, 240, 245)

### Testing

Test the generated model:

```bash
python3 test_greek_temple.py
```

This will verify:
- ✓ File exists and is valid
- ✓ Correct GLB format
- ✓ Proper mesh structure
- ✓ Reasonable dimensions
- ✓ Model sits on the ground plane

## Viewing the Model

### Option 1: Use the 3D Model Viewer Platform

1. Start the Flask application:
   ```bash
   python3 app.py
   ```

2. Open your browser to `http://localhost:5001`

3. Upload the file `uploads/greek_temple.glb`

4. View and interact with the 3D temple:
   - **Rotate**: Left mouse button + drag
   - **Zoom**: Mouse scroll wheel
   - **Pan**: Right mouse button + drag

### Option 2: Use Any GLB Viewer

The generated GLB file is compatible with any glTF/GLB viewer, including:
- [gltf-viewer.donmccurdy.com](https://gltf-viewer.donmccurdy.com/)
- Blender (File → Import → glTF 2.0)
- Three.js applications
- Babylon.js applications
- Unity (with glTF importer)
- Unreal Engine (with glTF importer)

## Architecture Details

The temple follows classical Greek architectural principles:

### Proportions
- **Column height to diameter ratio**: 15:1 (typical of Doric order)
- **Intercolumniation**: Regular spacing between columns
- **Platform height**: Approximately 1.5 units (typical 3-step base)

### Layout
- **Hexastyle front**: 6 columns across the front facade
- **Peripteral design**: Columns surrounding the entire building
- **Rectangular cella**: Inner sanctuary chamber
- **Gabled roof**: Triangular pediment on front and back

### Historical Accuracy
This temple is inspired by famous Greek temples such as:
- The Parthenon (Athens)
- Temple of Hephaestus (Athens)
- Temple of Poseidon (Sounion)

## Customization

You can modify the `generate_greek_temple.py` script to customize:

- **Dimensions**: Adjust `platform_width`, `platform_depth`, `column_height`
- **Number of columns**: Change `num_front_columns` and `num_side_columns`
- **Column style**: Modify `column_radius` and add more details
- **Colors**: Change the `vertex_colors` values
- **Roof shape**: Adjust `pediment_height` for steeper or flatter roofs

Example modifications:

```python
# Make a larger temple
platform_width = 30
platform_depth = 18

# Add more columns
num_front_columns = 8

# Taller columns
column_height = 8

# Different color (e.g., sandstone)
combined.visual.vertex_colors = [245, 222, 179, 255]
```

## File Structure

```
generate_greek_temple.py  # Main generator script
test_greek_temple.py      # Test suite for the model
uploads/                  # Output directory
└── greek_temple.glb      # Generated 3D model
```

## Technical Details

The model is created using parametric geometry:
- **Cylinders** for columns (24 segments for smooth appearance)
- **Boxes** for the platform, entablature, and cella
- **Custom meshes** for the triangular pediments and roof slopes
- **Vertex coloring** for uniform appearance

All meshes are combined into a single GLB file for efficient loading and rendering.

## Troubleshooting

### Issue: Model appears too small or large in viewer

**Solution**: The model uses relative units. Most 3D viewers will auto-scale. If needed, adjust the viewing distance in your 3D viewer or modify the scale in the generator script.

### Issue: Model appears dark

**Solution**: Ensure your 3D viewer has proper lighting. The model has a light color and requires adequate scene lighting to be visible.

### Issue: Import error when running the script

**Solution**: Make sure all dependencies are installed:
```bash
pip install trimesh numpy pygltflib
```

### Issue: File not found error

**Solution**: The script creates an `uploads/` directory automatically. Ensure you have write permissions in the current directory.

## License

This generator script is part of the 3D Model Viewer Platform project and follows the same MIT License.

## Credits

- **Architecture**: Inspired by ancient Greek temples
- **3D Library**: Built with Trimesh
- **Format**: glTF 2.0 (GLB binary)

---

**Ready to explore ancient architecture in 3D!** 🏛️
