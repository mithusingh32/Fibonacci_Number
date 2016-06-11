#Print out the Fiboancci number at any location in the sequnce
#You also can make it so the entire squence is reutrned

def fibNum(howManyPlaces):
    ls = [0,1]
    first =0
    
    while first < howManyPlaces-1:
        i = len(ls)
        nextValue = ls[i-1] + ls[i-2]
        ls.append(nextValue)
        first += 1
        
    #return ls
    return int(ls[howManyPlaces])
