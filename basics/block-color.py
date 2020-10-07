import bpy
from random import randint

""" # Check if script is opened in Blender program
import os, sys
if(bpy.context.space_data == None):
    cwd = os.path.dirname(os.path.abspath(__file__))
else:
    cwd = os.path.dirname(bpy.context.space_data.text.filepath)
# Get folder of script and add current working directory to path
sys.path.append(cwd)
import utils """

def cleanUp():
# cleanUp:  delete anything I may have created the last time I ran a script

    # Deselect any objects I might have selected before running this script
    bpy.ops.object.select_all(action='DESELECT')

    # Delete all of the Mesh objects
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

cleanUp()

bpy.ops.mesh.primitive_cube_add(location=(randint( -3, 3 ), randint( -3, 3 ),randint( -3, 3 )))
cube = bpy.context.object

obj = bpy.context.object  # Select the active object.
mat = bpy.data.materials.new(name='Material')  # Create a material.
mat.diffuse_color = ( round (randint(-10, 10)/10),round (randint(-10, 10)/10),round (randint(-10, 10)/10), 1 )
obj.data.materials.append(mat)  # Assign the new material.

print("here we go")
print(cube)
print(bpy.context.object)

# mymat = bpy.data.materials.new("Red")
# mymat.diffuse_color = ( 1.0, 0.0, 0.0, 1 )
# cube.materials.append(mymat)


""" 
Commands generated by my following the Blender Materials tutorial:
bpy.context.space_data.context = 'MATERIAL'
bpy.ops.material.new()
bpy.context.object.active_material.name = "Strawberry"

# Base color
bpy.data.materials["Strawberry"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.0190628, 0.153036, 1)

# Roughness
bpy.data.materials["Strawberry"].node_tree.nodes["Principled BSDF"].inputs[7].default_value = 0.333935
 """

# ---------------------------------------------------------------------------------------
# mat.diffuse_color = ( 1.0, 0.0, 0.0, 1 )
# mat.diffuse_shader = 'LAMBERT'    # Error:Material object has no such attribute
# Settings for the material go here.


# Set the new material you just created to the ico sphere's active material.
# cube.active_material = mat


""" 

mat = bpy.data.materials.new(name= 'colored')

# Save the ico sphere you just created in a variable.
ico = bpy.data.objects['Icosphere']

# Set the new material you just created to the ico sphere's active material.
ico.active_material = mat

# Let's define the colors that we're going to use. Each color is defines as a 4-tuple
# where each of the four values is a float number between 0 and 1. The numbers are for
# red, green, blue and alpha respectively. Our object is going to be fully opaque, so
# alpha is always set to 1. The colors are stored in a list.
colors = [(1, .7, .2, 1), # golden
          (.1, 1, .1, 1), # green
          (.1, .7, 1, 1), # blue
          (.7, 0, 1, 1), # purple
          (1, 0, 0, 1), # red
          (0, 0, 0, 1) # black
          ]

# Let's create a list of all the frames along the timeline where you want to insert keyframes.
# There will be as many keyframes as colors in the colors list because we want to change colors
# at these locations on the Timeline.         
frames = [1, 30, 60, 90, 120, 250]

# Now let's insert the keyframes. We can do it in a for loop. The loop will iterate over both 
# frames and colors, so we need two loop variables (f for frames and c for colors). 
# Besides we have to zip the two lists using the zip function.
for f, c in zip(frames, colors):
    # Set the material's diffuse color to the current color from the colors list.
    mat.diffuse_color = c
 """