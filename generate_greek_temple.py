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
    dark_green = np.array([34, 80, 40, 255], dtype=np.uint8)
    light_green = np.array([144, 238, 144, 255], dtype=np.uint8)
    tile_blue = np.array([65, 125, 180, 255], dtype=np.uint8)
    pot_clay = np.array([210, 140, 70, 255], dtype=np.uint8)
    
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
        # Add fluting
        for i in range(20):
            flute_angle = i * 2 * np.pi / 20
            flute = trimesh.creation.cylinder(radius=column_radius * 0.05, height=column_height)
            flute.apply_translation([x + (column_radius - 0.05) * np.cos(flute_angle), 5 + (column_radius - 0.05) * np.sin(flute_angle), platform_top + column_height/2])
            flute.visual.vertex_colors[:] = marble_white
            meshes.append(flute)
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
        # Add fluting
        for i in range(20):
            flute_angle = i * 2 * np.pi / 20
            flute = trimesh.creation.cylinder(radius=column_radius * 0.05, height=column_height)
            flute.apply_translation([x + (column_radius - 0.05) * np.cos(flute_angle), -5 + (column_radius - 0.05) * np.sin(flute_angle), platform_top + column_height/2])
            flute.visual.vertex_colors[:] = marble_white
            meshes.append(flute)
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
        # Add fluting
        for i in range(20):
            flute_angle = i * 2 * np.pi / 20
            flute = trimesh.creation.cylinder(radius=column_radius * 0.05, height=column_height)
            flute.apply_translation([-8 + (column_radius - 0.05) * np.cos(flute_angle), y + (column_radius - 0.05) * np.sin(flute_angle), platform_top + column_height/2])
            flute.visual.vertex_colors[:] = marble_white
            meshes.append(flute)
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
        # Add fluting
        for i in range(20):
            flute_angle = i * 2 * np.pi / 20
            flute = trimesh.creation.cylinder(radius=column_radius * 0.05, height=column_height)
            flute.apply_translation([8 + (column_radius - 0.05) * np.cos(flute_angle), y + (column_radius - 0.05) * np.sin(flute_angle), platform_top + column_height/2])
            flute.visual.vertex_colors[:] = marble_white
            meshes.append(flute)
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
    
    # ALTAR - Central altar for offerings
    altar = trimesh.creation.box([2, 1, 1])
    altar.apply_translation([0, 0, platform_top + 0.55])
    altar.visual.vertex_colors[:] = marble_white
    meshes.append(altar)
    
    # INTERNAL WALLS - Add some internal partitions for detail
    internal_wall1 = trimesh.creation.box([0.2, 8, 2])
    internal_wall1.apply_translation([-3, 0, platform_top + 1])
    internal_wall1.visual.vertex_colors[:] = marble_white
    meshes.append(internal_wall1)
    internal_wall2 = trimesh.creation.box([0.2, 8, 2])
    internal_wall2.apply_translation([3, 0, platform_top + 1])
    internal_wall2.visual.vertex_colors[:] = marble_white
    meshes.append(internal_wall2)
    
    # INDOOR POOL - Enhanced with better design
    pool_width = 8
    pool_depth = 4
    pool_basin_height = 1.5
    
    # Pool basin structure - positioned lower
    pool_basin = trimesh.creation.box([pool_width + 0.2, pool_depth + 0.2, pool_basin_height])
    pool_basin.apply_translation([0, 0, platform_top - pool_basin_height/2 - 0.2])
    pool_basin.visual.vertex_colors[:] = pool_gray
    meshes.append(pool_basin)
    
    # Pool water - larger, deeper, more visible
    water = trimesh.creation.box([pool_width - 0.6, pool_depth - 0.6, 0.8])
    water.apply_translation([0, 0, platform_top - 0.5])
    water.visual.vertex_colors[:] = water_blue
    meshes.append(water)
    
    # Additional water layer for depth effect
    water_deep = trimesh.creation.box([pool_width - 0.8, pool_depth - 0.8, 0.3])
    water_deep.apply_translation([0, 0, platform_top - 0.9])
    water_deep.visual.vertex_colors[:] = np.array([40, 100, 150, 255], dtype=np.uint8)
    meshes.append(water_deep)
    
    # Decorative pool rim with detail
    pool_rim = trimesh.creation.box([pool_width + 0.8, pool_depth + 0.8, 0.4])
    pool_rim.apply_translation([0, 0, platform_top + 0.2])
    pool_rim.visual.vertex_colors[:] = marble_white
    meshes.append(pool_rim)
    
    # Inner pool border decoration
    pool_border = trimesh.creation.box([pool_width + 0.3, pool_depth + 0.3, 0.15])
    pool_border.apply_translation([0, 0, platform_top - 0.1])
    pool_border.visual.vertex_colors[:] = tile_blue
    meshes.append(pool_border)
    
    # Pool corner decorations (small pillars)
    corner_positions = [
        (pool_width/2 + 0.4, pool_depth/2 + 0.4),
        (pool_width/2 + 0.4, -pool_depth/2 - 0.4),
        (-pool_width/2 - 0.4, pool_depth/2 + 0.4),
        (-pool_width/2 - 0.4, -pool_depth/2 - 0.4),
    ]
    for x, y in corner_positions:
        corner_pillar = trimesh.creation.cylinder(radius=0.25, height=0.7)
        corner_pillar.apply_translation([x, y, platform_top + 0.35])
        corner_pillar.visual.vertex_colors[:] = gold
        meshes.append(corner_pillar)
        
        # Corner capital
        corner_cap = trimesh.creation.cylinder(radius=0.35, height=0.2)
        corner_cap.apply_translation([x, y, platform_top + 0.75])
        corner_cap.visual.vertex_colors[:] = gold
        meshes.append(corner_cap)
    
    # Pool tiling pattern - decorative tiles
    tile_size = 0.6
    for i in np.arange(-pool_width/2 + 0.3, pool_width/2, tile_size):
        for j in np.arange(-pool_depth/2 + 0.3, pool_depth/2, tile_size):
            tile = trimesh.creation.box([tile_size - 0.12, tile_size - 0.12, 0.08])
            tile.apply_translation([i, j, platform_top - 0.45])
            tile.visual.vertex_colors[:] = tile_blue if (int(i*10) + int(j*10)) % 2 == 0 else np.array([100, 180, 220, 255], dtype=np.uint8)
            meshes.append(tile)
    
    # Enhanced steps into pool with railings
    step_width = 3.0
    step_depth = 0.7
    for i in range(5):
        step = trimesh.creation.box([step_width, step_depth, 0.3])
        step_z = platform_top - 0.8 + i * 0.25
        step_y = pool_depth/2 + 1.5 + i * step_depth
        step.apply_translation([0, step_y, step_z])
        step.visual.vertex_colors[:] = marble_white
        meshes.append(step)
        
        # Step railings - thicker and more prominent
        for side_x in [-step_width/2 - 0.2, step_width/2 + 0.2]:
            railing = trimesh.creation.cylinder(radius=0.12, height=0.6)
            railing.apply_translation([side_x, step_y, step_z + 0.35])
            railing.visual.vertex_colors[:] = gold
            meshes.append(railing)
    
    # GREENERY - Expanded potted plants around temple
    plant_positions = [
        (-10, 7, 1.7),
        (10, 7, 1.7),
        (-10, -7, 1.7),
        (10, -7, 1.7),
        (-11, 0, 1.7),
        (11, 0, 1.7),
        (-8, 9, 1.7),
        (8, 9, 1.7),
        (-8, -9, 1.7),
        (8, -9, 1.7),
    ]
    
    for px, py, pz in plant_positions:
        # Pot
        pot = trimesh.creation.cylinder(radius=0.45, height=0.7)
        pot.apply_translation([px, py, pz])
        pot.visual.vertex_colors[:] = pot_clay
        meshes.append(pot)
        
        # Pot rim
        pot_rim = trimesh.creation.cylinder(radius=0.5, height=0.12)
        pot_rim.apply_translation([px, py, pz + 0.4])
        pot_rim.visual.vertex_colors[:] = np.array([190, 120, 50, 255], dtype=np.uint8)
        meshes.append(pot_rim)
        
        # Plant foliage (spheres) - larger and bushier
        foliage = trimesh.creation.icosphere(radius=0.75, subdivisions=3)
        foliage.apply_translation([px, py, pz + 1.0])
        foliage.visual.vertex_colors[:] = dark_green
        meshes.append(foliage)
        
        # Secondary foliage for bushiness
        foliage2 = trimesh.creation.icosphere(radius=0.55, subdivisions=3)
        foliage2.apply_translation([px + 0.4, py + 0.3, pz + 0.8])
        foliage2.visual.vertex_colors[:] = light_green
        meshes.append(foliage2)
        
        # Tertiary foliage
        foliage3 = trimesh.creation.icosphere(radius=0.45, subdivisions=2)
        foliage3.apply_translation([px - 0.3, py - 0.2, pz + 0.9])
        foliage3.visual.vertex_colors[:] = dark_green
        meshes.append(foliage3)
    
    # EXPANDED GARDEN AREA - Ground greenery patches
    garden_color = np.array([80, 140, 60, 255], dtype=np.uint8)
    for gx in np.arange(-12, 13, 2.5):
        for gy in np.arange(-10, 11, 2.5):
            if (abs(gx) > 8 or abs(gy) > 6):  # Only around edges
                garden_patch = trimesh.creation.box([2.0, 2.0, 0.08])
                garden_patch.apply_translation([gx, gy, 0.35])
                garden_patch.visual.vertex_colors[:] = garden_color
                meshes.append(garden_patch)
    
    # Decorative shrubs throughout garden
    shrub_positions = [
        (-12, 5), (-12, -5), (12, 5), (12, -5),
        (-6, 10), (-6, -10), (6, 10), (6, -10),
        (-4, 11), (4, 11), (-4, -11), (4, -11),
    ]
    
    for sx, sy in shrub_positions:
        shrub = trimesh.creation.icosphere(radius=0.5, subdivisions=2)
        shrub.apply_translation([sx, sy, 0.7])
        shrub.visual.vertex_colors[:] = light_green
        meshes.append(shrub)
        
        # Shrub base
        shrub_base = trimesh.creation.cylinder(radius=0.3, height=0.4)
        shrub_base.apply_translation([sx, sy, 0.3])
        shrub_base.visual.vertex_colors[:] = np.array([60, 100, 40, 255], dtype=np.uint8)
        meshes.append(shrub_base)
    
    # DECORATIVE COLUMNS - Add ornamental elements
    # Column bases with stepped design
    for x in front_positions:
        base_step = trimesh.creation.box([1.0, 1.0, 0.2])
        base_step.apply_translation([x, 5, platform_top - 0.3])
        base_step.visual.vertex_colors[:] = marble_white
        meshes.append(base_step)
    
    for x in front_positions:
        base_step = trimesh.creation.box([1.0, 1.0, 0.2])
        base_step.apply_translation([x, -5, platform_top - 0.3])
        base_step.visual.vertex_colors[:] = marble_white
        meshes.append(base_step)
    
    # ORNAMENTAL BORDER - Around entablature
    border_height = 0.3
    entablature_z = platform_top + column_height + 0.5
    border_z = entablature_z + entablature_height + border_height/2
    
    border_front = trimesh.creation.box([17, 0.4, border_height])
    border_front.apply_translation([0, 5.5, border_z])
    border_front.visual.vertex_colors[:] = gold
    meshes.append(border_front)
    
    border_back = trimesh.creation.box([17, 0.4, border_height])
    border_back.apply_translation([0, -5.5, border_z])
    border_back.visual.vertex_colors[:] = gold
    meshes.append(border_back)
    
    border_left = trimesh.creation.box([0.4, 11, border_height])
    border_left.apply_translation([-8.5, 0, border_z])
    border_left.visual.vertex_colors[:] = gold
    meshes.append(border_left)
    
    border_right = trimesh.creation.box([0.4, 11, border_height])
    border_right.apply_translation([8.5, 0, border_z])
    border_right.visual.vertex_colors[:] = gold
    meshes.append(border_right)
    
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
    
    temple = create_perfect_temple(target_position=(0.0, -0.0, 0.0))
    
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
        print(f"   ✅ 16 proper columns with gold capitals and fluting")
        print(f"   ✅ Triangular pitched roof")
        print(f"   ✅ Indoor pool with marble rim")
        print(f"   ✅ Steps leading into pool")
        print(f"   ✅ Central altar")
        print(f"   ✅ Internal walls for detail")
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