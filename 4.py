import urllib2

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
init_nbr = 12345


result = urllib2.urlopen(base_url + str(init_nbr)).read()

for i in range(400):
    next_nbr=result.split(' ')[-1]
    result = urllib2.urlopen(base_url + str(next_nbr)).read()
    print result
