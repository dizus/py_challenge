import urllib2
import zipfile
import StringIO

urlcontent = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip").read()
mem_file = StringIO.StringIO( urlcontent )

zip_obj = zipfile.ZipFile( mem_file, mode='r' )

content=zip_obj.read("90052.txt");
comments=""

for i in range(907):
    next_file_nbr = content.split(' ')[-1]
    next_file_name = next_file_nbr + ".txt"
    content=zip_obj.read( next_file_name )
    comments += zip_obj.getinfo( next_file_name ).comment

print comments


