"""
Group 1 - Insertion Sort

a       b   c           d       e
0           current
"""

mylist = [1,20,3,4,2,100,15,99]
def insertsort(mylist):
    lastsorted = 0
    for currentindex in range(0,len(mylist)): # loop through each position
        
        print"\nindex pass: " + str(currentindex) + " start with: "
        print str(mylist)
        startindex = currentindex
        for i in range(lastsorted-1,-1,-1):
            if mylist[i] > mylist[startindex]:
                mylist[i],mylist[startindex] = mylist[startindex],mylist[i] # swap!
                startindex -= 1
                print "  "+str(mylist)
        lastsorted += 1
    print mylist
        
        

insertsort(mylist)
        