#Prints out the howManyPlaces down Fibonacci number

def fibNum(howManyPlaces):
    #Fibancci Number
    ls = [0,1]
    first =0
    
    while first < howManyPlaces-1:
        i = len(ls)
        #print ">>> length of ls %d" %i
        nextValue = ls[i-1] + ls[i-2]
        ls.append(nextValue)
        #print ">>> List LS %r" %ls
        first += 1
        
    return int(ls[howManyPlaces])

print fibNum(25)