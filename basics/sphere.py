import bpy
from math import pi
from mathutils import Euler
tau = 2*pi

bpy.ops.mesh.primitive_ico_sphere_add(location=(1, 1, 1))
ball = bpy.context.object
