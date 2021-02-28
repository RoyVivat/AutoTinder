
from PIL import Image  
import os

dirname = os.path.dirname(__file__)
pic_dir = os.path.join(dirname, "pics/helen_1")

for filename in os.listdir(pic_dir):
    im = Image.open(filename)  
    im.show()
    delay(2000)

