# Example from https://il.pycon.org/2016/static/sessions/tamir-lousky.pdf

import bpy
from random import randint

# Generate 50 cubes in random locations
for i in range(50):
    bpy.ops.mesh.primitive_cube_add(
    location = [ randint( -10, 10 ) for axis in 'xyz' ] 
    )