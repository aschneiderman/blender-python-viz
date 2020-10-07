import bpy

bpy.data.objects["Cube"].data.vertices[0].co.x += 2.0


bpy.ops.mesh.primitive_cube_add(location=(1, 0, 0))