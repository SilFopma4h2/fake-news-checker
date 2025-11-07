"""
Greek Temple 3D Model Generator

This script generates a clean 3D model of a Greek temple with:
- A raised platform (stylobate)
- Doric columns arranged in a peristyle
- A triangular pediment roof (gable)
- Clean geometric design typical of ancient Greek architecture

The generated model is saved as a GLB file compatible with the 3D Model Viewer.
"""
import trimesh
import numpy as np
from pathlib import Path


def create_cylinder(radius, height, segments=32):
    """Create a cylinder mesh."""
    return trimesh.creation.cylinder(radius=radius, height=height, sections=segments)


def create_box(dimensions):
    """Create a box mesh with given dimensions [width, depth, height]."""
    return trimesh.creation.box(extents=dimensions)


def create_greek_temple():
    """
    Create a complete Greek temple 3D model.
    
    Returns:
        trimesh.Trimesh: Combined mesh of the entire temple
    """
    meshes = []
    
    # ============ BASE PLATFORM (STYLOBATE) ============
    # Three-tiered platform that the temple sits on
    platform_width = 20
    platform_depth = 12
    
    # Bottom tier (largest)
    base1 = create_box([platform_width + 1, platform_depth + 1, 0.5])
    base1.apply_translation([0, 0, 0.25])
    meshes.append(base1)
    
    # Middle tier
    base2 = create_box([platform_width + 0.5, platform_depth + 0.5, 0.5])
    base2.apply_translation([0, 0, 0.75])
    meshes.append(base2)
    
    # Top tier (stylobate)
    base3 = create_box([platform_width, platform_depth, 0.5])
    base3.apply_translation([0, 0, 1.25])
    meshes.append(base3)
    
    # ============ COLUMNS ============
    column_radius = 0.4
    column_height = 6
    column_segments = 24  # More segments for smoother columns
    
    # Column positions (arranged in a rectangle around the temple)
    # Front and back rows (6 columns each - typical of Greek temples)
    front_back_positions = []
    num_front_columns = 6
    column_spacing = (platform_width - 2) / (num_front_columns - 1)
    
    for i in range(num_front_columns):
        x = -((platform_width - 2) / 2) + i * column_spacing
        # Front row
        front_back_positions.append([x, (platform_depth / 2) - 1.5, 1.5 + column_height / 2])
        # Back row
        front_back_positions.append([x, -(platform_depth / 2) + 1.5, 1.5 + column_height / 2])
    
    # Side columns (excluding corners as they're already in front/back)
    num_side_columns = 4  # Additional columns on each side
    side_spacing = (platform_depth - 3) / (num_side_columns - 1)
    
    for i in range(1, num_side_columns - 1):  # Exclude first and last (corners)
        y = -((platform_depth - 3) / 2) + i * side_spacing
        # Left side
        front_back_positions.append([-(platform_width / 2) + 1.5, y, 1.5 + column_height / 2])
        # Right side
        front_back_positions.append([(platform_width / 2) - 1.5, y, 1.5 + column_height / 2])
    
    # Create all columns
    for pos in front_back_positions:
        column = create_cylinder(column_radius, column_height, segments=column_segments)
        column.apply_translation(pos)
        meshes.append(column)
        
        # Add capital (top of column) - slightly wider
        capital = create_cylinder(column_radius * 1.3, 0.4, segments=column_segments)
        capital.apply_translation([pos[0], pos[1], pos[2] + column_height / 2 + 0.2])
        meshes.append(capital)
        
        # Add base (bottom of column) - slightly wider
        base = create_cylinder(column_radius * 1.2, 0.3, segments=column_segments)
        base.apply_translation([pos[0], pos[1], pos[2] - column_height / 2 - 0.15])
        meshes.append(base)
    
    # ============ ENTABLATURE (Structure above columns) ============
    entablature_height = 1.5
    entablature = create_box([platform_width - 1, platform_depth - 1, entablature_height])
    entablature.apply_translation([0, 0, 1.5 + column_height + entablature_height / 2])
    meshes.append(entablature)
    
    # ============ ROOF (PEDIMENT) ============
    roof_height = 3
    roof_base_z = 1.5 + column_height + entablature_height
    
    # Main roof (rectangular prism sloped)
    roof_length = platform_width - 0.5
    roof_width = platform_depth + 1
    
    # Create triangular pediment on front and back
    pediment_height = 2.5
    pediment_base_width = platform_width - 1
    
    # Front pediment (triangle)
    vertices_front = np.array([
        [-pediment_base_width / 2, platform_depth / 2 - 1, roof_base_z],
        [pediment_base_width / 2, platform_depth / 2 - 1, roof_base_z],
        [0, platform_depth / 2 - 1, roof_base_z + pediment_height],
        [-pediment_base_width / 2, platform_depth / 2 - 1.5, roof_base_z],
        [pediment_base_width / 2, platform_depth / 2 - 1.5, roof_base_z],
        [0, platform_depth / 2 - 1.5, roof_base_z + pediment_height],
    ])
    
    faces_front = np.array([
        [0, 1, 2],  # Front triangle
        [3, 5, 4],  # Back triangle
        [0, 3, 4], [0, 4, 1],  # Bottom
        [0, 2, 5], [0, 5, 3],  # Left side
        [1, 4, 5], [1, 5, 2],  # Right side
    ])
    
    front_pediment = trimesh.Trimesh(vertices=vertices_front, faces=faces_front)
    meshes.append(front_pediment)
    
    # Back pediment
    vertices_back = vertices_front.copy()
    vertices_back[:, 1] = -vertices_back[:, 1]  # Mirror across y-axis
    back_pediment = trimesh.Trimesh(vertices=vertices_back, faces=faces_front)
    meshes.append(back_pediment)
    
    # Roof slopes (connecting the pediments)
    # Left slope
    left_roof_vertices = np.array([
        [-pediment_base_width / 2, platform_depth / 2 - 1, roof_base_z],
        [-pediment_base_width / 2, -(platform_depth / 2 - 1), roof_base_z],
        [0, -(platform_depth / 2 - 1), roof_base_z + pediment_height],
        [0, platform_depth / 2 - 1, roof_base_z + pediment_height],
    ])
    left_roof_faces = np.array([[0, 1, 2], [0, 2, 3]])
    left_roof = trimesh.Trimesh(vertices=left_roof_vertices, faces=left_roof_faces)
    meshes.append(left_roof)
    
    # Right slope
    right_roof_vertices = np.array([
        [pediment_base_width / 2, platform_depth / 2 - 1, roof_base_z],
        [pediment_base_width / 2, -(platform_depth / 2 - 1), roof_base_z],
        [0, -(platform_depth / 2 - 1), roof_base_z + pediment_height],
        [0, platform_depth / 2 - 1, roof_base_z + pediment_height],
    ])
    right_roof_faces = np.array([[0, 2, 1], [0, 3, 2]])
    right_roof = trimesh.Trimesh(vertices=right_roof_vertices, faces=right_roof_faces)
    meshes.append(right_roof)
    
    # ============ CELLA (Inner chamber/room) ============
    cella_width = platform_width - 6
    cella_depth = platform_depth - 4
    cella_height = column_height - 1
    
    cella = create_box([cella_width, cella_depth, cella_height])
    cella.apply_translation([0, 0, 1.5 + cella_height / 2])
    meshes.append(cella)
    
    # Combine all meshes
    combined = trimesh.util.concatenate(meshes)
    
    # Set a uniform color (white/marble-like)
    # Create array of colors with shape (n_vertices, 4)
    color = np.array([240, 240, 245, 255], dtype=np.uint8)
    combined.visual.vertex_colors = np.tile(color, (len(combined.vertices), 1))
    
    return combined


def main():
    """Generate and save the Greek temple model."""
    print("Generating Greek Temple 3D model...")
    
    # Create the temple
    temple = create_greek_temple()
    
    # Create output directory if it doesn't exist
    output_dir = Path("uploads")
    output_dir.mkdir(exist_ok=True)
    
    # Save as GLB file
    output_file = output_dir / "greek_temple.glb"
    temple.export(output_file, file_type='glb')
    
    print(f"✅ Greek temple model generated successfully!")
    print(f"📁 Saved to: {output_file}")
    print(f"📊 Model stats:")
    print(f"   - Vertices: {len(temple.vertices)}")
    print(f"   - Faces: {len(temple.faces)}")
    print(f"   - Bounds: {temple.bounds}")
    print(f"\n💡 You can now upload this file to the 3D Model Viewer platform!")


if __name__ == "__main__":
    main()
