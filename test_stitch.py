import cv2
import argparse
import sys
from utils import stitch

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
	help="comma delimited paths to input images to stitch")
ap.add_argument("-o", "--output", type=str, required=False, default="output.png",
	help="path to the output image")
args = vars(ap.parse_args())
image_paths = args["images"].split(",")

images = []
for i, image_path in enumerate(image_paths, 1):
    image = cv2.imread(image_path)
    images.append(image)

stitched = stitch(images)

output_filename = args["output"]
cv2.imwrite(output_filename, stitched)

