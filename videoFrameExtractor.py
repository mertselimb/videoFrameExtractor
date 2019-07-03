import os
import cv2


directory = "./videos"
directories = [directory, "./output"]

for d in directories:
    if not(os.path.isdir(d)):
        os.mkdir(d)
        
if not os.listdir(directory) :
    raise Exception("Videos directory is empty.")

f = 1
for filename in os.listdir(directory):
	print(str(f) + ". file.")
	print("Working on: " + filename)
	videoPath = os.path.join(directory, filename)

	name = os.path.splitext(filename)[0]
	outputDir = "./output/" + name + "/"
	if not(os.path.isdir(outputDir)):
		os.mkdir(outputDir)
	vidcap = cv2.VideoCapture(videoPath)
	success,image = vidcap.read()
	count = 0
	while success:
		cv2.imwrite(outputDir + "frame%d.jpg" % count, image)
		success,image = vidcap.read()
		count = count + 1
	f = f + 1

print("Everything succesfully completed.")



