import urllib.request
from io import BytesIO
from PIL import Image

image_data_arr = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()
image_mem_file = BytesIO(image_data_arr)
image = Image.open(image_mem_file)

line_to_read = int(image.size[1]/2)
for i in range( 0,image.size[0],7 ):
    cur_char = image.getpixel((i,line_to_read))[0]
    print ( chr(cur_char), end=''  )


print ()

arr=[105, 110, 116, 101, 103, 114, 105, 116, 121]

for i in range( len(arr) ):
    print (chr(arr[i]),end='')
