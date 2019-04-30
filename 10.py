
seq = [ 21 ]
for i in range(0,30):
    spoken_count=0
    next_el=""
    it = str(seq[i])[0]
    for nbr in str( seq[i] ):
        if  nbr == it :
            spoken_count += 1
        else:
            next_el += str(spoken_count*10 + int(it)) 
            it = nbr
            spoken_count = 1

    next_el  += str(spoken_count*10 + int(it))

    seq.append( int(next_el) )

print (len(str(seq[28])))
