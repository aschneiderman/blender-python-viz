# test_module: code to make sure that importing a module while running a Blendeer script will work

import bpy

# Append the directory of the current script in Blender to the system path, so Python will be able to import my modules
import os, sys
sys.path.append( os.path.dirname(bpy.context.space_data.text.filepath) )

print("hi there")

import my_module
my_module.test()
