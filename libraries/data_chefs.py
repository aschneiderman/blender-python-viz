# data_chefs: library to simplify building creative DataViz using Blender
# 
# NOTE: to import tthis module when running a Python script in Blender:
# import os, sys
# sys.path.append( os.path.dirname('../libraries'))
# import data_chefs as dc

import bpy

print ("\n\n---------------------------------------------------------------------------------------\nhere we go...\n")
print("\nsuccessfully imported Data Chefs\n")

def clean_up():
# clean_up:  delete anything I may have created the last time I ran a script

    # Deselect any objects I might have selected before running this script
    bpy.ops.object.select_all(action='DESELECT')

    # Delete all of the Mesh objects
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

