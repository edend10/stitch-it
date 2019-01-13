import cv2
import argparse
import sys
from utils import stitch

CV_CAP_PROP_POS_FRAMES = 1
CV_CAP_PROP_FRAME_COUNT = 7

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str, required=True,
	help="path to input video to stitch")
ap.add_argument("-s", "--frame_step", type=int, required=False, default=50,
	help="number of frames to skip between frame samples")
ap.add_argument("-o", "--output", type=str, required=False, default="output.png",
	help="path to the output image")
args = vars(ap.parse_args())

video_path = args["video"]
frame_step = args["frame_step"]
output_filename = args["output"]

vid_cap = cv2.VideoCapture(video_path)
num_frames = int(vid_cap.get(CV_CAP_PROP_FRAME_COUNT))

images = []
for i in range(0, num_frames, frame_step):
    vid_cap.set(CV_CAP_PROP_POS_FRAMES, i)
    ret, frame = vid_cap.read()
    if frame is not None:
        images.append(frame)

stitched = stitch(images)

cv2.imwrite(output_filename, stitched)
