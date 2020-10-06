import bpy
from mathutils import *
D = bpy.data
C = bpy.context





# bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))


print(bpy.data.objects)

bpy.data.objects["Cube"].data.vertices[0].co.x += 3.0

print("blaaaaaaaaaaaaaaaaaasaaabbbbb\n\ntest\nPtest")



