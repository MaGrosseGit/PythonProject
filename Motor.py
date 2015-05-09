import bpy

tagWindow = "Window"
tagWindowAsset = "Cube001"
tagDoor = "Door"

class GenerateType:
	"""Classe pour chaque type d'asset:
	- La liste d'asset disponible
	- La liste d'empty pour les placer
	- le nombre d'empty
	- le tag des assets"""

    
	def __init__(self, tag):
		"""Constructeur de notre classe"""
		        
		self.tag = tag
		self.listTargets = [obj for obj in bpy.context.scene.objects if obj.name.startswith(self.tag)]
		self.nbtarget = len(self.listTargets)
		self.listAssets = self.ChooseAssets()
        

	def ChooseAssets(self): #Add asset's list instead of cube creation process
		assets = []
		for i in range(0,self.nbtarget) :
			bpy.ops.mesh.primitive_cube_add()
			mesh = bpy.context.object
			mesh.name = self.tag+ "_asset.001"
			assets.append(mesh)
		return assets   

	def PlaceObject(self, obj,target):
		obj.location = target.location
		obj.rotation_euler = target.rotation_euler  
		
	def PlaceAllObjects(self):
		for i in range(0,self.nbtarget) :
			self.PlaceObject(self.listAssets[i],self.listTargets[i])
        
	


windows = GenerateType(tagWindow)
windows.PlaceAllObjects()

doors = GenerateType(tagDoor)
doors.PlaceAllObjects()









