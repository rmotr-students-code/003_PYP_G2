def insertion(lst):
    length = len(lst)
    for i in range(1, length):
        item = lst[i]
        index = i
        while index > 0 and lst[index-1] > item:
            lst[index] = lst[index-1]
            index -= 1
            
        lst[index] = item
    print lst
    return lst

if __name__ == "__main__":
    print "started"
    assert(insertion([1,3,5,4,2])==[1,2,3,4,5])
    assert(insertion([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]) == [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])
    print "done"