import time

# for each number (in the range) simple parsing 
def parseInput():
    # with open("e2.txt", "r") as f:
    with open("2.txt", "r") as f:
        s = f.read().split(",")
        return s

# function that handles finding bad ids. calls check function 
def findBadIds(r):
    badNums = []
    for s in r:
        bounds = s.split('-')
        start, end = bounds[0], bounds[1]
        # print('testing', start, 'and', end) # test we can read bounds
        # if end < start:
            # print('end < start case') # random edge case just in case
        
        i = int(start)
        while i <= int(end):
            res = checkCase(str(i)) # check if number satisfies the case
            if res != 0:
                badNums.append(res)
            i += 1

    return badNums

# given an int (len of string), return an array of numbers that fit inside it 
def findLensToCheck(l):
    lens = []
    i = 1
    # print('testing length', l)
    while i < l: 
        if l % i == 0:
            lens.append(i)
            # print('length', i, 'fits without remainder')
        i += 1

    return lens

# splits into front and half, checks if those halves are identical
# but in p2 we will need to change this to check for any repetition of numbers
def checkCase(s):
    strlen = int(len(s))
    patternLens = findLensToCheck(strlen)
    badIds = []

    # extract this to another function 
    for subLen in patternLens:
        # print('sublen test is ', subLen)
        parts = [s[i:i + subLen] for i in range(0, len(s), subLen)] # split str into equal length
        # print(parts)
        equal = True

        # compare the start of segment to rest of it 
        for p in parts:
            if parts[0] != p:
                equal = False
                # continue
        
        if equal == True:
            # print(s, 'is bad num')
            badIds.append(int(s))

    if len(badIds) == 0:
        return 0
    else:
        return badIds[0]
            
## main 
startT = time.perf_counter()
r = parseInput()
badIds = findBadIds(r)
# print(badIds)
res = 0
for i in badIds:
    res += i

print(res)
print('time', time.perf_counter() - startT)
# wow my solution is slow? 