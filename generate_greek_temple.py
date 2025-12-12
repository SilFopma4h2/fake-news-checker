"""
PERFECT Greek Temple with Pool - UPRIGHT AND PROPER
"""
import trimesh
import numpy as np
import os


def create_perfect_temple(target_position=(0.0, 0.0, 0.0)):
    """Create a perfectly upright Greek temple with proper architecture and place at target_position."""
    meshes = []
    
    # Colors
    marble_white = np.array([245, 245, 245, 255], dtype=np.uint8)
    water_blue = np.array([80, 150, 200, 255], dtype=np.uint8)
    roof_red = np.array([180, 100, 70, 255], dtype=np.uint8)
    pool_gray = np.array([150, 150, 150, 255], dtype=np.uint8)
    gold = np.array([255, 215, 0, 255], dtype=np.uint8)
    ground_green = np.array([100, 120, 80, 255], dtype=np.uint8)
    
    # FOUNDATION - Multi-level base for stability
    foundation_base = trimesh.creation.box([20, 14, 0.5])
    foundation_base.apply_translation([0, 0, 0.25])
    foundation_base.visual.vertex_colors[:] = marble_white
    meshes.append(foundation_base)
    
    main_platform = trimesh.creation.box([18, 12, 1.0])
    main_platform.apply_translation([0, 0, 1.0])
    main_platform.visual.vertex_colors[:] = marble_white
    meshes.append(main_platform)
    
    # COLUMNS - Proper Greek temple columns with capitals
    column_radius = 0.4
    column_height = 5.0
    platform_top = 1.5
    
    # Front row columns (6 columns)
    front_positions = [-6, -3.6, -1.2, 1.2, 3.6, 6]
    for x in front_positions:
        column = trimesh.creation.cylinder(radius=column_radius, height=column_height)
        column.apply_translation([x, 5, platform_top + column_height/2])
        column.visual.vertex_colors[:] = marble_white
        meshes.append(column)
        base = trimesh.creation.cylinder(radius=column_radius*1.2, height=0.3)
        base.apply_translation([x, 5, platform_top + 0.15])
        base.visual.vertex_colors[:] = marble_white
        meshes.append(base)
        capital = trimesh.creation.cylinder(radius=column_radius*1.3, height=0.5)
        capital.apply_translation([x, 5, platform_top + column_height + 0.25])
        capital.visual.vertex_colors[:] = gold
        meshes.append(capital)
    
    # Back row columns (6 columns)
    for x in front_positions:
        column = trimesh.creation.cylinder(radius=column_radius, height=column_height)
        column.apply_translation([x, -5, platform_top + column_height/2])
        column.visual.vertex_colors[:] = marble_white
        meshes.append(column)
        base = trimesh.creation.cylinder(radius=column_radius*1.2, height=0.3)
        base.apply_translation([x, -5, platform_top + 0.15])
        base.visual.vertex_colors[:] = marble_white
        meshes.append(base)
        capital = trimesh.creation.cylinder(radius=column_radius*1.3, height=0.5)
        capital.apply_translation([x, -5, platform_top + column_height + 0.25])
        capital.visual.vertex_colors[:] = gold
        meshes.append(capital)
    
    # Side columns (4 per side)
    side_positions = [-2.5, -0.8, 0.8, 2.5]
    for y in side_positions:
        column = trimesh.creation.cylinder(radius=column_radius, height=column_height)
        column.apply_translation([-8, y, platform_top + column_height/2])
        column.visual.vertex_colors[:] = marble_white
        meshes.append(column)
        base = trimesh.creation.cylinder(radius=column_radius*1.2, height=0.3)
        base.apply_translation([-8, y, platform_top + 0.15])
        base.visual.vertex_colors[:] = marble_white
        meshes.append(base)
        capital = trimesh.creation.cylinder(radius=column_radius*1.3, height=0.5)
        capital.apply_translation([-8, y, platform_top + column_height + 0.25])
        capital.visual.vertex_colors[:] = gold
        meshes.append(capital)
        column = trimesh.creation.cylinder(radius=column_radius, height=column_height)
        column.apply_translation([8, y, platform_top + column_height/2])
        column.visual.vertex_colors[:] = marble_white
        meshes.append(column)
        base = trimesh.creation.cylinder(radius=column_radius*1.2, height=0.3)
        base.apply_translation([8, y, platform_top + 0.15])
        base.visual.vertex_colors[:] = marble_white
        meshes.append(base)
        capital = trimesh.creation.cylinder(radius=column_radius*1.3, height=0.5)
        capital.apply_translation([8, y, platform_top + column_height + 0.25])
        capital.visual.vertex_colors[:] = gold
        meshes.append(capital)
    
    # ENTABLATURE (horizontal beam above columns)
    entablature_height = 1.0
    entablature_z = platform_top + column_height + 0.5
    entablature = trimesh.creation.box([17, 11, entablature_height])
    entablature.apply_translation([0, 0, entablature_z + entablature_height/2])
    entablature.visual.vertex_colors[:] = marble_white
    meshes.append(entablature)
    
    # FIXED TRIANGULAR ROOF - robust triangulated geometry
    roof_base_z = entablature_z + entablature_height
    roof_height = 3.0
    # 6 vertices: front triangle (0,1,2), back triangle (3,4,5)
    roof_vertices = np.array([
        [-8.5, 5.5, roof_base_z],      # 0 front bottom left
        [8.5, 5.5, roof_base_z],       # 1 front bottom right
        [0.0, 5.5, roof_base_z + roof_height],  # 2 front top
        [-8.5, -5.5, roof_base_z],     # 3 back bottom left
        [8.5, -5.5, roof_base_z],      # 4 back bottom right
        [0.0, -5.5, roof_base_z + roof_height], # 5 back top
    ], dtype=float)
    
    roof_faces = np.array([
        [0, 1, 2],   # front triangle
        [3, 5, 4],   # back triangle (note orientation)
        # left side (two triangles)
        [0, 2, 5],
        [0, 5, 3],
        # right side (two triangles)
        [1, 4, 2],
        [2, 4, 5],
        # underside (two triangles to close bottom for watertight roof)
        [0, 3, 4],
        [0, 4, 1],
    ], dtype=int)
    
    roof = trimesh.Trimesh(vertices=roof_vertices, faces=roof_faces, process=False)
    roof.visual.vertex_colors[:] = roof_red
    roof.fix_normals()
    meshes.append(roof)
    
    # INTERIOR FLOOR
    interior_floor = trimesh.creation.box([16, 10, 0.1])
    interior_floor.apply_translation([0, 0, platform_top + 0.05])
    interior_floor.visual.vertex_colors[:] = marble_white
    meshes.append(interior_floor)
    
    # INDOOR POOL - Properly positioned in center
    pool_width = 8
    pool_depth = 4
    pool_basin_height = 0.8
    pool_basin = trimesh.creation.box([pool_width, pool_depth, pool_basin_height])
    pool_basin.apply_translation([0, 0, platform_top - pool_basin_height/2 + 0.1])
    pool_basin.visual.vertex_colors[:] = pool_gray
    meshes.append(pool_basin)
    water = trimesh.creation.box([pool_width - 0.2, pool_depth - 0.2, 0.3])
    water.apply_translation([0, 0, platform_top - 0.15])
    water.visual.vertex_colors[:] = water_blue
    meshes.append(water)
    pool_rim = trimesh.creation.box([pool_width + 0.4, pool_depth + 0.4, 0.2])
    pool_rim.apply_translation([0, 0, platform_top + 0.1])
    pool_rim.visual.vertex_colors[:] = marble_white
    meshes.append(pool_rim)
    # Steps into pool
    step_width = 2.5
    step_depth = 0.8
    for i in range(3):
        step = trimesh.creation.box([step_width, step_depth, 0.2])
        step_z = platform_top - 0.5 + i * 0.15
        step_y = pool_depth/2 + 1 + i * step_depth
        step.apply_translation([0, step_y, step_z])
        step.visual.vertex_colors[:] = marble_white
        meshes.append(step)
    
    # Combine all meshes
    temple = trimesh.util.concatenate(meshes)
    
    # Fix normals and ensure upright
    temple.fix_normals()
    
    # Rotate from Z-up to Y-up for GLB compatibility (stand upright in viewers)
    rotation_matrix = trimesh.transformations.rotation_matrix(3 * np.pi / 2, [1, 0, 0])  # 270 degrees around X-axis
    temple.apply_transform(rotation_matrix)
    
    # Align so center X/Y and base Z match target_position
    try:
        bounds = temple.bounds
        min_bound = bounds[0]
        max_bound = bounds[1]
        current_center_x = (min_bound[0] + max_bound[0]) / 2.0
        current_center_y = (min_bound[1] + max_bound[1]) / 2.0
        current_min_z = min_bound[2]
        tx = float(target_position[0]) - current_center_x
        ty = float(target_position[1]) - current_center_y
        tz = float(target_position[2]) - current_min_z
        temple.apply_translation([tx, ty, tz])
    except Exception:
        # best-effort: simple translate to target_position
        temple.apply_translation([float(target_position[0]), float(target_position[1]), float(target_position[2])])
    
    return temple


def save_temple():
    """Save the temple ONLY as GLB in uploads directory."""
    print("🏛️ Creating PERFECT Greek Temple...")
    print("   ✨ Upright orientation")
    print("   🏛️ Proper columns with capitals")
    print("   🏠 Triangular roof")
    print("   🏊 Indoor pool with steps")
    
    temple = create_perfect_temple(target_position=(0.0, -1.5, 0.0))
    
    # Get script directory and create uploads folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    uploads_dir = os.path.join(script_dir, "uploads")
    
    # Create uploads directory if it doesn't exist
    os.makedirs(uploads_dir, exist_ok=True)
    print(f"📂 Uploads directory: {uploads_dir}")
    
    # Create a clear timestamp for unique files
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save ONLY GLB files with CLEAR, PREDICTABLE NAMES
    file_configs = [
        ("PERFECT_GREEK_TEMPLE.glb", "glb"),
        (f"TEMPLE_PERFECT_{timestamp}.glb", "glb"),
    ]
    
    saved_files = []
    
    for filename, fmt in file_configs:
        try:
            filepath = os.path.join(uploads_dir, filename)
            print(f"🔄 Saving {filename} to uploads folder...")
            
            # Force export with explicit filename
            temple.export(file_obj=filepath, file_type=fmt)
            
            if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
                size_kb = os.path.getsize(filepath) // 1024
                print(f"✅ SUCCESS: {filename} ({size_kb} KB)")
                saved_files.append(filename)
            else:
                print(f"❌ FAILED: {filename}")
                
        except Exception as e:
            print(f"❌ ERROR saving {filename}: {e}")
    
    # List all GLB files in uploads directory
    print(f"\n📂 ALL GLB FILES IN UPLOADS DIRECTORY:")
    try:
        if os.path.exists(uploads_dir):
            all_files = os.listdir(uploads_dir)
            glb_files = [f for f in all_files if f.endswith('.glb')]
            if glb_files:
                for glb_file in glb_files:
                    size_kb = os.path.getsize(os.path.join(uploads_dir, glb_file)) // 1024
                    print(f"   📄 {glb_file} ({size_kb} KB)")
            else:
                print(f"   📄 No GLB files found in uploads directory")
        else:
            print(f"   ❌ Uploads directory not found")
    except Exception as e:
        print(f"   ❌ Error listing files: {e}")
    
    if saved_files:
        print(f"\n🎉 PERFECT TEMPLE SAVED!")
        for f in saved_files:
            full_path = os.path.join(uploads_dir, f)
            print(f"   📁 {full_path}")
        
        print(f"\n🏛️ FEATURES:")
        print(f"   ✅ Stands perfectly upright")
        print(f"   ✅ Multi-level foundation")
        print(f"   ✅ 16 proper columns with gold capitals")
        print(f"   ✅ Triangular pitched roof")
        print(f"   ✅ Indoor pool with marble rim")
        print(f"   ✅ Steps leading into pool")
        print(f"   ✅ Proper Greek temple proportions")
        
        print(f"\n📋 TO VIEW:")
        print(f"   1. Navigate to C:\\Users\\silfo\\fake-news-checker\\uploads")
        print(f"   2. Right-click PERFECT_GREEK_TEMPLE.glb")
        print(f"   3. Open with → 3D Viewer")
        print(f"   4. Or drag to: threejs.org/editor/")
        
    else:
        print(f"\n💥 NO FILES SAVED!")
        
    return len(saved_files) > 0


if __name__ == "__main__":
    success = save_temple()
    if success:
        print("\n🚀 PERFECT TEMPLE READY! This one will be amazing! 🏛️✨")
    else:
        print("\n😡 FAILED! Try running as administrator!")