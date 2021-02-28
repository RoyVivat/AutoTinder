import numpy as np
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from PIL import Image  
import os
import time

def transform_images(pic_path, tpic_path, size = (256, 256)):
    for filename in os.listdir(pic_path):
        #filename = os.listdir(pic_path)[0]
        im = Image.open(os.path.join(pic_path,filename))

        if(im.height < im.width):
            im = im.crop(((im.width-im.height)/2, 0, (im.width-im.height)/2 + im.height, im.height))
        else:
            im = im.crop((0, (im.height-im.width)/2, im.width, (im.height-im.width)/2 + im.width))
        im.thumbnail(size)
        im.save(os.path.join(tpic_path, filename))

dirname = os.path.dirname(__file__)
pic_dir = os.path.join(dirname, "pics/helen_1")
tpic_dir = os.path.join(dirname, "pics/transformed_images")

#transform_images(pic_dir, tpic_dir)


# Preprocess images into one-hot-encoding vectors

# Construct Neural Network Model

