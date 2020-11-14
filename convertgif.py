import os
from PIL import Image

activedir = 'C:/Users/keith/Desktop/Brandywine20/images'
destinationdir = 'C:/Users/keith/Desktop/Brandywine20/jpg'

for filename in os.listdir(activedir):
	if filename.endswith(".gif"):
		imagelocation = activedir + "/" + filename
		imagedestination = destinationdir + "/" + filename[:-3] + "png"
		activeimg = Image.open(imagelocation)
		activeimg.save(imagedestination)
	else:
		continue