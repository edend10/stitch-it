import cv2
import argparse
import sys
from utils import stitch, extract_frames
from ocr_utils import extract_text

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str, required=True,
	help="path to input video to stitch")
ap.add_argument("-t", "--frame_param_type", type=str, required=False, default='target',
	help="'target' to target number of frame samples, or 'step' to determine how many to skip between samples")
ap.add_argument("-p", "--frame_param", type=int, required=False, default=8,
	help="if type is 'target' then number of frame samples, if type is 'step' number of frames to skip between frame samples")
ap.add_argument("-o", "--output", type=str, required=False, default="output.png",
	help="path to the output image")
args = vars(ap.parse_args())

video_path = args["video"]
frame_param_type = args["frame_param_type"]
frame_param = args["frame_param"]
output_filename = args["output"]

images = extract_frames(video_path, frame_param_type, frame_param)
stitched = stitch(images)

content = extract_text(stitched)

with open(output_filename, "w") as f:
    f.write(content)
