import cv2
vidcap = cv2.VideoCapture('fisheye.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./frames/frame%d.jpg" % count, image)    
  success,image = vidcap.read()
  count += 1
