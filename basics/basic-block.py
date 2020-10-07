import bpy
from random import randint


def cleanUp():
# cleanUp:  delete anything I may have created the last time I ran a script

    # Deselect any objects I might have selected before running this script
    bpy.ops.object.select_all(action='DESELECT')

    # Delete all of the Mesh objects
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

cleanUp()
bpy.ops.mesh.primitive_cube_add(location=(randint( -3, 3 ), randint( -3, 3 ),randint( -3, 3 )))



