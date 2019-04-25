import urllib2
from StringIO import StringIO
from PIL import Image


image_data_arr = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()
image_mem_file = StringIO(image_data_arr)
image_arr = Image.open(image_mem_file).getdata()

print chr(image_arr[int(len( image_arr )/2)][0])
