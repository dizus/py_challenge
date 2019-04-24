
import pickle

file_obj = open( "5.obj", "r")
obj = pickle.load(file_obj)

for line in obj:
    for chars in line:
        print chars[0]*(chars[1]-1),
    print;

