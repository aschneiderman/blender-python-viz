import bpy
from math import pi, radians
from mathutils import Euler
import os
import random

p = os.path.dirname(__file__)
PATH = os.path.dirname(p) #os.getcwd()
OUTPUT_PATH = os.path.join(PATH,"output")

print(f"Path: {PATH}")

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)


def removeAll(type=None):
    # Possible type: �MESH�, �CURVE�, �SURFACE�, �META�, �FONT�, �ARMATURE�, �LATTICE�, �EMPTY�, �CAMERA�, �LAMP�
    if type:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type=type)
        bpy.ops.object.delete()
    else:
        # Remove all elements in scene
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete(use_global=False)
        

# http://web.purplefrog.com/~thoth/blender/python-cookbook/load-image-texture.html
def material_for_texture(name, path):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.image = bpy.data.images.load(path)
    mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
    return mat


def floor(mat):
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(0,0,0))
    pl = bpy.context.object
    pl.name = 'ground'
    pl.scale = (100, 100, 0.1)
    pl.data.materials.append(mat)
    bpy.ops.rigidbody.object_add(type='PASSIVE')
    
def base_block(mat, rotation, location, scale, is_cube):
    location2 = [location[0] - 6, location[1] + 7, location[2]]
    footprint = scale[:]
    
    if rotation[0]:
        footprint = (footprint[0],footprint[2],footprint[1])
        
    if rotation[1]:
        footprint = (footprint[2],footprint[1],footprint[0])
    
    if rotation[2]:
        footprint = (footprint[1],footprint[0],footprint[2])
    
    x = location2[0] + (footprint[0]/2)
    y = location2[1] - (footprint[1]/2) 
    z = location2[2] + (footprint[2]/2)

    if is_cube:
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, z))
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 4
        bpy.context.object.modifiers["Bevel"].profile = .8
    else:    
        bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=1, enter_editmode=False, 
            align='WORLD', location=(x, y, z))

    bpy.ops.rigidbody.object_add()
    block1 = bpy.context.object
    block1.rigid_body.type = 'ACTIVE'    
    block1.scale = scale
    block1.data.materials.append(mat)
    
    rotation2 = [(radians(90) if c else 0) for c in rotation]
        
    block1.rotation_euler = Euler(rotation2, 'XYZ')

def red_block(location, rotation):
    base_block(red_mat, rotation, location, (4,2,1), True)
    
def yellow_block(location, rotation):
    base_block(yellow_mat, rotation, location, (8,2,1), True)



  
def render(filename):
    rnd = bpy.data.scenes['Scene'].render
    rnd.resolution_x = 1280
    rnd.resolution_y = 720
    rnd.resolution_percentage = 100
    rnd.filepath = os.path.join(OUTPUT_PATH, filename)
    bpy.ops.render.render(animation=False, write_still=True)
    

def init():
    removeAll(�MESH�)
    #reset_blend()


    
    floor(floor_mat)

# Create a material.
floor_mat = material_for_texture("Mat-red", os.path.join(PATH,"wood-floor.jpg"))
red_mat = material_for_texture("Mat-red", os.path.join(PATH,"wood-red.png"))

init()
    red_block((0,0,0), (False, False, False) )
    red_block((0,0,4), (False, False, False) )
