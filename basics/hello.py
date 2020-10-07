import bpy
from mathutils import *
D = bpy.data
C = bpy.context

# NOTE:: a module in the same directory doesn't work in Blender
# import test
# print(strawberry())

def strawberry(value):
    return 42

print(strawberry("Test"))


bpy.ops.mesh.primitive_cube_add(location=(1, 0, 0))


print(bpy.data.objects)

bpy.data.objects["Cube"].data.vertices[0].co.x += 2.0

print("blaaaaaaaaaaaaaaaaaasaaabbbbb\n\ntest\nPtest")




