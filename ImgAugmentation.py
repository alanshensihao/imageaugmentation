import os, sys
import cv2
import numpy as np
from matplotlib import pyplot
from numpy import expand_dims
from PIL import Image
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import ChangeImageName

# GLOBAL CONSTANT
RGB2GRAY = 1
RGB2HSV = 2


# # rename image names in order
# renameimage = ChangeImageName.RenameImage.renameImage()
# if renameimage:
# 	print("images renamed sucessfully")
# else:
# 	print("images already renamed")


# root directory of the project
ROOT_DIR = os.path.abspath(".")
path_access = os.access(ROOT_DIR,os.W_OK)
print("Access to write the file:", path_access) 


IMAGE_PATH = os.path.join(ROOT_DIR,"0001.jpg")

# load the image
img = load_img(IMAGE_PATH)
# report details about the image
print(type(img))
print(img.format)
print(img.mode)
print(img.size)

# convert to numpy array
image = np.array(img)

#preprocessing_function for more features in imagedatagenerator
class SwitchPreprocessMode(object):
	def num_colormode(self, image, colormode):
		if colormode == 1:
			method_name = 'RGB_to_GRAY'
		if colormode == 2:
			method_name = 'RGB_to_HSV'
		method = getattr(self,method_name,lambda: "Invalid colormode")
		return method()
	def RGB_to_GRAY(self):
		return Image.fromarray(cv2.cvtColor(image,cv2.COLOR_RGB2GRAY))
	def RGB_to_HSV(self):
		return Image.fromarray(cv2.cvtColor(image,cv2.COLOR_RGB2HSV))		

def img2array(img123, color_code):
	a = SwitchPreprocessMode()
	if color_code == "HSV":
		new_image = np.array((a.num_colormode(img123,RGB2HSV)))
	if color_code == "GRAY":
		new_image = np.array((a.num_colormode(img123,RGB2GRAY)))
	if color_code == "original":
		new_image = np.array(img123)
	return new_image

# #test the image before adding the rank
# test = Image.fromarray(img2array(img,"GRAY"))
# test.show()

def array_rank_up(img123, color_code):
	imagedata = np.array(img2array(img123,color_code))
	if color_code == "HSV":
		sample = expand_dims(imagedata,0)
	elif color_code == "GRAY":
		sample = expand_dims(imagedata,(0,-1))
	elif color_code == "original":
		sample = expand_dims(imagedata,0)
	return sample

# # check dimension
# test = array_rank_up(img,"GRAY")

# create a random image data augmentation method
def image_data_generator(randnum):
	if randnum == 1:
	# create image data augmentation generator 1
		datagen = ImageDataGenerator(
			featurewise_center=True,
			featurewise_std_normalization=True,
			rotation_range=20,
			width_shift_range=[-50,50])
	elif randnum == 2:
	# create image data augmentation generator 2
		datagen = ImageDataGenerator(
			rotation_range=40,
			height_shift_range= 100)
	elif randnum == 3:
	# create image data augmentation generator 3
		datagen = ImageDataGenerator(
			rotation_range=60,
			width_shift_range=[-100,100])
	return datagen

datagen = image_data_generator(np.random.randint(1,3))

# # prepare iterator
# # generate samples and plot

def each_image(img1,color_code):
	for i in range(3):
		# define subplot
		pyplot.subplot(330 + 1 + i)
		# generate batch of images
		batch = img1.next()
		# convert to unsigned integers for viewing
		image = batch[0].astype('uint8')
		# plot raw pixel data
		if color_code == "GRAY":
			if image.ndim == 3:
				image = image[:,:,0]
			pyplot.imshow(image,cmap='gray')
		elif color_code =="HSV":
			pyplot.imshow(image,cmap='hsv')
		else:
			pyplot.imshow(image)
	return 0

it1 = datagen.flow(array_rank_up(img,"original"), batch_size=1)
it2 = datagen.flow(array_rank_up(img,"HSV"), batch_size=1)
it3 = datagen.flow(array_rank_up(img,"GRAY"), batch_size=1)



# imagedata = img2array(image,'GRAY')
# pyplot.imshow(imagedata,cmap='gray')
# pyplot.show()

# batch = it3.next()
# # convert to unsigned integers for viewing
# image = batch[0].astype('uint8')
# image_drop = image[:,:,0]
# print(image.shape)
# print()
# print(image.size)
# pyplot.imshow(image_drop,cmap='gray')
# pyplot.show()



# test = array_rank_up(img,"GRAY")
# test.show()

each_image(it1,"original")
pyplot.show()
each_image(it2,"HSV")
pyplot.show()
each_image(it3,"GRAY")

# # show the figure
pyplot.show()






# it = datagen.flow(samples, batch_size=1)
# # generate samples and plot
# for i in range(9):
# 	# define subplot
# 	pyplot.subplot(330 + 1 + i)
# 	# generate batch of images
# 	batch = it.next()
# 	# convert to unsigned integers for viewing
# 	image = batch[0].astype('uint8')
# 	# plot raw pixel data
# 	pyplot.imshow(image)
# # show the figure
# pyplot.show()

