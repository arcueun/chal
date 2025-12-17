# find the biggest number in the string and save it 
# find the second biggest number in the string *after* the number we just found.

# um, no, it doesn't, it fails if the biggest number is at the end of the string
# is this really a o(n^2) approach surely not 
# lets go for that for now 
# starting with the first number, compare it in comparison with every other number in that string 
# repeat for every single one

# find the 3 biggest numbers in the array 
# find their positions 
# find the configuration of the 3 numbers that produces the biggest number 
    # of digits abc
    # ab, ac, bc, ac 

def read_input():
    # with open("e3.txt", "r") as f:
    with open("3.txt", "r") as f:
        s = f.read().split()
        i = 0
        # print(s)
        # for r in s:
        #     print(i, r) # ensure we split properly
        #     i += 1
        return s

def findLargestJolts(s):
    biggestJolts = 0
    tens = s[0]
    ones = s[1]
    biggestJolts = int(tens + ones)
    i = 2
    while i < len(s):
        # ab already exists, and we see int C join us. 
        # so we check if bc > biggestJolts 
        if int(ones + s[i]) > biggestJolts:
            # if so, update biggestJolts 
            biggestJolts = int(ones + s[i])
            tens = ones
            ones = s[i]

        # and then if ac > biggestJolts 
        elif int(tens + s[i]) > biggestJolts:
            # just update ones 
            ones = s[i]
            biggestJolts = int(tens+s[i])

        i += 1

    return biggestJolts

    
## main 
batteryRows = read_input()
totalPower = 0
for row in batteryRows:
    print(row, end=' ')
    totalPower += findLargestJolts(row)

print('total power:', totalPower)