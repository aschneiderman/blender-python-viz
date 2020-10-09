import bpy
from random import randint


def cleanUp():
    # Gets more complicated:
    # https://blender.stackexchange.com/questions/27234/python-how-to-completely-remove-an-object
    # https://docs.blender.org/api/current/bpy.ops.html#overriding-context

    # Deselect all
    bpy.ops.object.select_all(action='DESELECT')

    # Delete all of the Mesh objects
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

cleanUp()
bpy.ops.mesh.primitive_cube_add(location=(randint( -3, 3 ), randint( -3, 3 ),randint( -3, 3 )))



