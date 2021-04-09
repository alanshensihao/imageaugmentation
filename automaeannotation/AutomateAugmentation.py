import json

import os 

import numpy as np

import cv2

import imgaug as ia
from imgaug.augmentables.polys import Polygon, PolygonsOnImage

def make_polys(json_file):
    with open(json_file, "r") as js:
        json_data = json.load(js)

    polys = []

    for shape in json_data['shapes']:
        # This assert might be overkill but better safe that sorry ...
        assert shape['shape_type'] == "polygon"
        polys.append(Polygon(shape['points'], label=shape['label']))

    img_shape = (json_data['imageHeight'], json_data['imageWidth'], 3)
    polys_oi = PolygonsOnImage(polys, shape=img_shape)
    return(polys_oi)


mug_img = cv2.imread("./40_json/img.png")

polys_oi = make_polys("40.json")

# This is just to plot it ...
overlay_mug = polys_oi.draw_on_image(mug_img)

cv2.imwrite("overlaid_mug.png", overlay_mug)

for i, p in enumerate(polys_oi):
    overlay_mug = p.draw_on_image(mug_img, color=(0, 0, 255))
    cv2.imwrite(f"over_p{i}mug.png", overlay_mug)

    
from imgaug import augmenters as iaa

my_augmenter = iaa.Sequential([
    iaa.GaussianBlur((0.1, 5)),
    iaa.Fliplr(0.5),
    iaa.Flipud(0.5),
    iaa.Rotate((-45,45))])

# If you pass the arguments, it returns 2 elements
# - The augmented Image
# - The augmented polygons 
augmented = my_augmenter(image = mug_img, polygons = polys_oi)
[type(x) for x in augmented]
# [<class 'numpy.ndarray'>, <class 'imgaug.augmentables.polys.PolygonsOnImage'>]

# So you can make a bunch of augmented image/polygon pairs
augmented_list = [my_augmenter(image = mug_img, polygons = polys_oi) for _ in range(10)]

i = 1
for img, polys in augmented_list:
    overlay_image = polys.draw_on_image(img)
    cv2.imwrite(f"{i}augmented_mug_polys.png", overlay_image)
    i = i+1


# # Now we just make the overlay for viz purposes
# overlaid_images = [polys.draw_on_image(img) for img, polys in augmented_list]

# cv2.imwrite("augmented_mug_polys.png", cv2.vconcat(overlaid_images))




mug_img = cv2.imread("./0_json/img.png")

polys_oi = make_polys("0.json")

# This is just to plot it ...
overlay_mug = polys_oi.draw_on_image(mug_img)

cv2.imwrite("overlaid_mug.png", overlay_mug)

for i, p in enumerate(polys_oi):
    overlay_mug = p.draw_on_image(mug_img, color=(0, 0, 255))
    cv2.imwrite(f"over_p{i}mug.png", overlay_mug)

    
from imgaug import augmenters as iaa

my_augmenter = iaa.Sequential([
    iaa.GaussianBlur((0.1, 5)),
    iaa.Fliplr(0.5),
    iaa.Flipud(0.5),
    iaa.Rotate((-45,45))])

# If you pass the arguments, it returns 2 elements
# - The augmented Image
# - The augmented polygons 
augmented = my_augmenter(image = mug_img, polygons = polys_oi)
[type(x) for x in augmented]
# [<class 'numpy.ndarray'>, <class 'imgaug.augmentables.polys.PolygonsOnImage'>]

# So you can make a bunch of augmented image/polygon pairs
augmented_list = [my_augmenter(image = mug_img, polygons = polys_oi) for _ in range(10)]

i = 1
for img, polys in augmented_list:
    overlay_image = polys.draw_on_image(img)
    cv2.imwrite(f"{i}augmented_mug_polys_1.png", overlay_image)
    i = i+1



