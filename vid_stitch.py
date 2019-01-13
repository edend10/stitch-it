import cv2
import argparse
import sys
from utils import stitch, extract_frames

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

images = extract_frames(video_path, frame_step)
stitched = stitch(images)

cv2.imwrite(output_filename, stitched)
