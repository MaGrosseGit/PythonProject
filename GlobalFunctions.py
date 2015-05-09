#initiating global functions
def GetNewParam(newMeshParam, originMeshParam, originMeshUnits) :
	return float(originMeshParam / (originMeshUnits/newMeshParam))

def DuplicateObject(name, copyobj, scene = bpy.context.scene):
 
	# Create new mesh
	mesh = bpy.data.meshes.new(name)
 
	# Create new object associated with the mesh
	ob_new = bpy.data.objects.new(name, mesh)
 
	# Copy data block from the old object into the new object
	ob_new.data = copyobj.data.copy()
	ob_new.scale = copyobj.scale
	ob_new.location = copyobj.location
 
	# Link new object to the given scene and select it
	scene.objects.link(ob_new)
	bpy.ops.object.select_all(action='DESELECT')
	ob_new.select = True
 
	return ob_new

def InstantiateMesh(mesh, name, position = vZero, rotation = rZero, clone = True) :
	if clone :
		newMesh = DuplicateObject(name, mesh)
	else :
		newMesh = bpy.context.object
		newMesh.name = name
	newMesh.location = position
	for i in range(3) :
		newMesh.rotation_euler[i] = math.radians(rotation[i])
	return newMesh

def InstantiatePrimitive(type, name, position = vZero, rotation = rZero, meshScale = sOne) :
	if type == "cube" :
		bpy.ops.mesh.primitive_cube_add()
	if type == "cylinder" :
		bpy.ops.mesh.primitive_cylinder_add()
	if type == "plane" :
		bpy.ops.mesh.primitive_plane_add()
	if type == "sphere" :
		bpy.ops.mesh.primitive_uv_sphere_add()
	newMesh = bpy.context.object
	newMesh = InstantiateMesh(newMesh, name, position, rotation, False)
	newMesh = bpy.context.object
	newMesh.scale = meshScale
	return newMesh

def DeleteMesh(mesh) :
	mesh.select = True   
	bpy.ops.object.delete(use_global=False)

def DeleteList(meshList, wtf = False) :
	#bpy.context.scene.objects.active.select = False
	bpy.ops.object.select_all(action='DESELECT')
	if wtf :
	   bpy.context.scene.objects.active = meshList[0]
	for mesh in meshList :
		mesh.select = True
	bpy.ops.object.delete(use_global=False)

def DeleteAll() :
	bpy.ops.object.select_all(action="DESELECT") 
	bpy.ops.object.select_all(action="TOGGLE") 
	bpy.ops.object.delete(use_global=True)

def JoinMesh(meshList, name = "", wtf = False) :
	bpy.context.scene.objects.active.select = False
	bpy.ops.object.select_all(action='DESELECT')
	if wtf :
	   bpy.context.scene.objects.active = meshList[0]
	for mesh in meshList :
		mesh.select = True
	bpy.ops.object.join()
	newMesh = bpy.context.object
	if name != "" :
		newMesh.name = name
	return newMesh
	
def JoinAll(name = "") :
	bpy.ops.object.select_all(action='DESELECT')
	bpy.ops.object.select_all(action="TOGGLE")
	bpy.ops.object.join()
	newMesh = bpy.context.object
	if name != "" :
		newMesh.name = name
	return newMesh

def ListToVector(list) :
	return mathutils.Vector((list[0], list[1], list[2]))
def VectorToList(vector) :
	return [vector.x, vector.y, vector.z]

def SubstractVectors(vector1, vector2) :
	result = [0,0,0]
	for i in range(3) :
		result[i] = vector1[i] - vector2[i]
	return result

def DivideVectors(vector1, divider) :
	result = [0,0,0]
	for i in range(3) :
		result[i] = vector1[i] / divider
	return result

def BVector(x,y,z) :
	return mathutils.Vector((x,y,z))

def GetPercent(value, percentage) :
	return (value*percentage)/100

def GetRandomValue(randomRange) :
	return random.uniform(randomRange[0], randomRange[1])