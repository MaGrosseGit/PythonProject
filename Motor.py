import bpy
import random

tagWindow = "Window"
tagWindowAsset = "Window_asset"
tagDoor = "Door"
uniqueAssets = False # If you what different asset on each empty



def duplicateObject(scene, name, copyobj):
 
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
    ob_new.select = True
 
    return ob_new




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
		self.listAssets = [obj for obj in bpy.context.scene.objects if obj.name.startswith("Asset_" + self.tag)] #Change with loaded list
		print (len(self.listAssets))
		self.listChoosenAssets = self.ChooseAssets()
		print (len(self.listChoosenAssets))
        

	def ChooseAssets(self):
		assets = []
		tempList = []
		for i in range(0,self.nbtarget) :
			tempInt = random.randint(0,len(self.listAssets)-1)
			if uniqueAssets :
				while tempInt in tempList :
					tempInt = random.randint(0,len(self.listAssets)-1)
				tempList.append(tempInt)
			mesh = duplicateObject(bpy.context.scene, "Asset_" + self.tag+ ".001", self.listAssets[tempInt])
			
			assets.append(mesh)
		return assets   

	def PlaceObject(self, obj,target):
		obj.location = target.location
		obj.rotation_euler = target.rotation_euler  
		maxDim = min(target.scale )*2
		multiplicator = maxDim / max(obj.dimensions)
		obj.dimensions = obj.dimensions *multiplicator
		
	def PlaceAllObjects(self):
		for i in range(0,self.nbtarget) :
			self.PlaceObject(self.listChoosenAssets[i],self.listTargets[i])
        
	


windows = GenerateType(tagWindow)
windows.PlaceAllObjects()



