# sphere: create a simple sphere
import bpy

# Import the Data Chefs library
import os, sys, importlib
sys.path.append('C:\\Users\\aschn\\Documents\\GitHub\\blender-python-viz\\libraries')
import data_chefs as dc
importlib.reload(dc)    # When I am developing the Data Chefs library, makes sure I am using the newest version


# Delete anything I may have created the last time I ran a script
dc.clean_up()

bpy.ops.mesh.primitive_ico_sphere_add(location=(1, 1, 1))
ball = bpy.context.object
