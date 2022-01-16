from defisheye import Defisheye

dtype = 'linear'
format = 'fullframe'
fov = 180
pfov = 120

#input image frame
img = "frame0.jpg"

#output image frame
img_out = f"frame_0.jpg.jpg"

obj = Defisheye(img, dtype=dtype, format=format, fov=fov, pfov=pfov)
obj.convert(img_out)
