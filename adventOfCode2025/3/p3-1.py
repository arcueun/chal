# iterate through an array, finding the highest joltage, that is, 
# two numbers of a string that create the largest integer without changing the numbers' order

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