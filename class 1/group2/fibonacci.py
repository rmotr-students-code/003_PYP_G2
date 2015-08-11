import sys

def iterative(n):
    a, b, i = 0, 1, 0
    if n == 0:
        return a
    if n == 1:
        return b
    while i < n:
        a, b = b, a+b
        i += 1
    return a

def recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive(n-1)+recursive(n-2)
    

def main():
    functionType = iterative
    if len(sys.argv) == 2:
        if sys.argv[1] == '--recursive':
            functionType = recursive

    while True:
        inp = raw_input('Enter the nth term of the Fibonacci sequence you want: ')
        try:
            n = int(inp)
        except ValueError:
            print "Please enter an integer, no alpha/punc"
            continue
        
        if n > 0:
            break
        else:
            print "Please enter an integer above 0"
    print functionType(n)


if __name__ == "__main__":
    main()
