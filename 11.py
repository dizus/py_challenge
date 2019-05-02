from PIL import Image
from io import BytesIO
from urllib import request
from math import ceil
import requests


username='huge'
password='file'
image_url='http://www.pythonchallenge.com/pc/return/cave.jpg'

response = requests.post( image_url,
                          auth=(username,password)
                          )

imagedata = Image.open(BytesIO(response.content) )

newimage = Image.new( imagedata.mode, (ceil(imagedata.size[0]/2)+1, ceil(imagedata.size[1]/2)+1) )
newimage_map = newimage.load()

for i in range(imagedata.size[0]):
    for j in range(imagedata.size[1]):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            newimage_map[ceil(i/2),ceil(j/2)] = imagedata.getpixel((i,j))

newimage.show()

