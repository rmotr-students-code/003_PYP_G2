def bubblesort(lst):
    length = len(lst)
    swapped = True
    j = 0
    while(swapped):
        swapped = False
        j+=1
        for i in range(length-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
    return lst


if __name__ == "__main__":
    print "started"
    assert(bubblesort([1,3,5,4,2])==[1,2,3,4,5])
    assert(bubblesort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]) == [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])
    print "done"