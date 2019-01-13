import numpy as np
import cv2
import sys

def rotate(img, angle):
    rows,cols,channels = img.shape
    axis_max = max(rows,cols)
    axis_min = min(rows,cols)
    axis_diff = (axis_max - axis_min) // 2
    empty_img = np.zeros([axis_max, axis_max, channels], dtype=np.uint8)
    if rows > cols:
        empty_img[:,axis_diff:axis_diff + axis_min] = img
    else:
        empty_img[axis_diff:axis_diff + axis_min, :] = img
    M = cv2.getRotationMatrix2D((axis_max / 2, axis_max / 2),angle,1)
    rotated_uncropped = cv2.warpAffine(empty_img, M, (axis_max, axis_max))
    if rows > cols:
        rotated_cropped = rotated_uncropped[axis_diff:axis_diff + axis_min,:]
    else:
        rotated_cropped = rotated_uncropped[:, axis_diff:axis_diff + axis_min]
    return rotated_cropped

def stitch(src_images):
    num_imgs = len(src_images)
    stitcher = cv2.createStitcher()
    stitched = []
    for i, image in enumerate(src_images, 1):
        rotated_img = rotate(image, 90)
        if stitched != []:
            images = [stitched]
            images.append(rotated_img)
            (status, stitched) = stitcher.stitch(images)
            if status == 0:
                print("stitched images %d/%d" % (i, num_imgs))
            else:
                sys.exit("Error stitching image %d/%d with status %d" % (i, num_imgs, status))
        else:
            stitched = rotated_img

    rotated_stitched = rotate(stitched, -90)
    return rotated_stitched

def stitch2(src_images):
    num_imgs = len(src_images)
    stitcher = cv2.createStitcher()
    stitched = []
    images = [rotate(img, 90) for img in src_images]
    images.reverse()
    (status, stitched) = stitcher.stitch(images)
    if status == 0:
        print("stitched %d images" % (num_imgs))
    else:
        sys.exit("Error stitching %d images with status %d" % (num_imgs, status))

    rotated_stitched = rotate(stitched, -90)
    return rotated_stitched
