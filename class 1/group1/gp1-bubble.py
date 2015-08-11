"""
Group 1 - Bubble Sort
example:
[20,3,5,1]
Pass 1:
[3,20,5,1] *flip! need another full pass
[3,5,20,1] *flip  <--- for optimization, track last flip
[3,5,1,20]  
Pass 2:
[3,5,1,20] (no change)
[3,1,5,20] *flip! need another pass
[3,1,5,20] (no change)
Pass 3:
[1,3,5,20] * had to flip here 
[1,3,5,20]
[1,3,5,20]
Pass 4:
[1,3,5,20], 3 times, no flips, mark as sorted.

optimizations:  


"""

def bubble_unoptimized(mylist,verbose):
    sorted = 0
    sortpass = 1
    while sorted == 0: #loop through a full pass of all number pairs and flip if necessary
        
        if verbose: print "pass " + str(sortpass) + "\n" + str(mylist) # for debugging
        
        flips = 0 # a flip anywhere in this pass indicates that we need another pass
        for i in range(0,len(mylist)-1):
            if mylist[i] > mylist[i+1]:
                mylist[i] , mylist[i+1] = mylist[i+1],mylist[i] #using python slicing trick to avoid temp var
                flips += 1
            if verbose: print "  " + str(mylist)
        if flips == 0: sorted = 1
        sortpass +=1 # for debugging
    print mylist
            
mylist = [1,3,50,7,29,4,56,2,57]
print "-------------Unoptimized BubbleSort--------------------"
bubble_unoptimized(mylist,0)




def bubble_simpleopt(mylist,verbose): # after each pass, the last element will always be correct.  Then last-1, etc.
    sorted = 0
    sortpass = 1
    list_length = len(mylist) #this will be decremented by 1 each pass for this optimization
    while sorted == 0: #loop through a full pass of all number pairs and flip if necessary
        
        if verbose: print "pass " + str(sortpass) + "\n" + str(mylist)
        
        flips = 0 # a flip anywhere in this pass indicates that we need another pass
        
        for i in range(0,list_length-1):
            if mylist[i] > mylist[i+1]:
                mylist[i] , mylist[i+1] = mylist[i+1],mylist[i] #using python slicing trick to avoid temp var
                flips += 1
            if verbose: print "  " + str(mylist)
        if flips == 0: sorted = 1
        sortpass +=1
        list_length -= 1 # !!! this is the entire optimization here really.  just shorten list by 1 per pass
    print mylist
            
mylist = [1,3,50,7,29,4,56,2,57]
print "-------------Optimized BubbleSort (shrink list length for each pass)--------------------"
bubble_simpleopt(mylist,0)



def bubble_optimized(mylist,verbose):
    sorted = 0
    sortpass = 1
    mylength = len(mylist)
    
    while sorted == 0: #loop through a full pass of all number pairs and flip if necessary
        
        if verbose: print "pass " + str(sortpass) + "\n" + str(mylist)
        
        flips = 0 # a flip anywhere in this pass indicates that we need another pass
        for i in range(0,mylength-1):
            if mylist[i] > mylist[i+1]:
                mylist[i] , mylist[i+1] = mylist[i+1],mylist[i] #using python slicing trick to avoid temp var
                flips += 1
                newlength =  i# !!! this is the secret to this optimization.  We shorten the length to the last flip index
                print "   flipped, setting finish to " + str(i)
            if verbose: print "  " + str(mylist)
        if flips == 0: sorted = 1
        sortpass +=1 # just for debugging
        mylength = newlength+1 # because we subtract 1 from it above
    print mylist
    
"""        
[1,3,50,2,100]

PASS 1  ( entire array )
0  1*,3,50,2,100   1,3,50,2,100
1  1,3*,50,2,100   1,3,50,2,100
2  1,3,50*,2,100   1,3,2,50,100  ** swap is marked  * marked newlength = 2
3  1,3,2,50*,100   1,3,2,50,100  no swap

PASS2  (only up to where the last swap was (which is newlength of 2 +1 is 3
will really iterate over range(0,mylength-1): which is 2+1-1 = 2

start with 1,3,2,50,100
pass 2:
0  1*,3,2,50,100    1*,3,2,50,100
1  1,3*,2,50,100    1,2,3,50,100  ** flip!  mark newlength = 1

pass 3:
0 1,2,3,50,100 , no flips, done.
"""  
            
mylist = [1,3,50,2,29,4,5,6,7]
print "-------------Optimize BubbleSort (remember where last swap was to cheat)--------------------"
bubble_optimized(mylist,1)