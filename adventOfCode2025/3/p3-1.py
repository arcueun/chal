# find the biggest number in the string and save it 
# find the second biggest number in the string *after* the number we just found.

# um, no, it doesn't, it fails if the biggest number is at the end of the string
# is this really a o(n^2) approach surely not 
# lets go for that for now 
# starting with the first number, compare it in comparison with every other number in that string 
# repeat for every single one

# find the 3 biggest numbers in the array 
# find their positions 

def read_input():
    with open("e3.txt", "r") as f:
    # with open("3.txt", "r") as f:
        s = f.read().split()
        i = 0
        for r in s:
            print(i, r) # ensure we split properly
            i += 1
        return s

def findBiggestNumbers(s):
    n1, n2, n3 = -1, -1, -1
    for i in s:
        num = int(i)
        if num > n1:
            n3 = n2
            n2 = n1
            n1 = num
    
        if num < n1 and num > n2:
            n3 = n2
            n2 = num

        if num < n2 and num > n3:
            n3 = num

    return n1, n2, n3

def locateBiggestNumbers(s, n1,n2,n3):
    l1, l2, l3 = -1,-1,-1
    i = 0
    while i < len(s):
        print(s[i])
        if s[i] == n1:
            l1 = i
        if s[i] == n2:
            l2 = i
        if s[i] == n3:
            l3 = i

        i += 1

    return l1, l2, l3

def findLargestJolts(string):
    n1, n2, n3 = findBiggestNumbers(string)
    l1, l2, l3 = locateBiggestNumbers(string, n1, n2, n3)
    print(n1, n2, n3)
    print('location', l1, l2, l3)
    
## main 
batteryRows = read_input()
totalPower = 0
for row in batteryRows:
    findLargestJolts(row)
