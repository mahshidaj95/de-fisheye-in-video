# de-fisheye-in-video

In this repository, we take an fisheye lens video as an input and convert it to the normal video.

After that, we use yolo object detection to detect moving objects in normal video.

First of all, we convert fisheye lens video to image frames with runing "video_to_frame.py". Then we run "defish.py" to convert fisheye lens image frames to normal image frames.

Finally we run "frame_to_video.py" to create output video.
