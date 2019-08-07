import os
import cv2
import math

directory = "./videos"
directories = [directory, "./output"]
expectedFrameRate = 7.5 # FPS of output
reportFrame = 100 # Report every 100 frames

for d in directories:
    if not(os.path.isdir(d)):
        os.mkdir(d)
        
if not os.listdir(directory) :
    raise Exception("Videos directory is empty.")

f = 1
for filename in os.listdir(directory):
	print("%d. file." % f)
	print("Working on: %s" % filename)
	videoPath = os.path.join(directory, filename)

	name = os.path.splitext(filename)[0]
	outputDir = "./output/" + name + "/"
	
	if not(os.path.isdir(outputDir)):
		os.mkdir(outputDir)

	vidcap = cv2.VideoCapture(videoPath)
	
	oldFPS = vidcap.get(cv2.CAP_PROP_FPS)
	print("Old FPS: %d New FPS: %d" %oldFPS, %expectedFrameRate)
	skipFrame = math.floor(oldFPS/expectedFrameRate) 
	print("Writing once every %d frames." % skipFrame)

	length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
	print("Frame count: %d" % length)


	success,image = vidcap.read()
	count = 0
	while success:
		if(count % skipFrame == 0):
			if(count % reportFrame == 0):
				print("At %d. frame" % count)
			cv2.imwrite(outputDir + "frame%d.jpg" % count, image)
		success,image = vidcap.read()
		count = count + 1
	f = f + 1

print("Everything succesfully completed.")



