import bpy
from mathutils import *
D = bpy.data
C = bpy.context

for i in range(0,3):
    bpy.ops.mesh.primitive_cube_add(location=(1, 2, i))

# Now all I need to be able to do is add a mouseclick and a control z command in blender, and I'm good to goP


