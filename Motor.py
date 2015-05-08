import bpy

tagWindow = "Window"
tagWindowAsset = "Cube001"
tagDoor = "Door"


def PlaceObject(obj,target):
    obj.location = target.location
    obj.rotation_euler = target.rotation_euler

def ChooseAssets(nbAsset,tag): #Add asset's list instead of cube creation process
	assets = []
	for i in range(0,nbAsset) :
		bpy.ops.mesh.primitive_cube_add()
		mesh = bpy.context.object
		mesh.name = tagWindowAsset + ".001"
		assets.append(mesh)
	return assets


scene = bpy.context.scene
window_targets= [obj for obj in scene.objects if obj.name.startswith(tagWindow)]
window_objs = ChooseAssets(len(window_targets),tagWindowAsset)
print (window_objs)

if len(window_targets) == len(window_objs) :
	for i in range(0,len(window_targets)) :
		PlaceObject(window_objs[i],window_targets[i])



