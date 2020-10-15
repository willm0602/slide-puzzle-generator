import random

def swap(spots):
    empty = spots.index(None)
    options = [-1,1,-4,4]
    if empty%4==0:
        options.remove(-1)
    if empty%4==3:
        options.remove(1)
    if empty < 4:
        options.remove(-4)
    if empty > 11:
        options.remove(4)
    delta = random.choice(options)
    if (empty+delta>=0) and (empty+delta<=15):  
        moving = empty + delta 
        spots[moving], spots[empty] = spots[empty], spots[moving]
        return(spots)
    else:
        return(swap(spots))

def shuffle(spots, n):
    for i in range(n):
        spots = swap(spots)
    return(spots)

spots = list(range(15))
spots.append(None)
spots = shuffle(spots,100)
