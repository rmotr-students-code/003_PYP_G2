"""
Group 1 - Fibonacci 
Write a program that generates the nth number in a fibonacci sequence 
(starting at 0). 
The program should start and ask two things:

The number that will describe the nth term you want to get
if the function should be recursive or not
The program should count with data validation. It means that the program must 
inform the user when the number she inserted is invalid.

Extra: If the user passes a --recursive argument, the program should not ask 
for the function to use and use the recursive function.
"""

def fibber(term, recursive):
    if recursive != 1:
        if term == 1: print 0
        elif term == 2: print 1
        else:
            oneback = 1
            twoback = 0
            counter = 2
            while counter < term:
                newfib = oneback + twoback
                #print newfib
                twoback = oneback
                oneback = newfib
                counter += 1
            print newfib
    if recursive:
        if term == 1:
            return 0
        elif term == 2:
            return 1
        else: #recursively return stuff
            return fibber(term-1,1)+fibber(term-2,1)
            #return fibber(term,1) + fibber(term-1,1)
            
# (((0 +1),+ 1,) + 2),+ 3, 5, 8
            #0 1 1 2 3*
 
print fibber(5,2) # 0


