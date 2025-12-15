import time

# read from file and present it as array of ranges
def parseInput():
    # with open("e2.txt", "r") as f:
    with open("2.txt", "r") as f:
        s = f.read().split(",")
        return s

# given ranges in array of ['aaaa-bbbb', 'cccc-dddd'] 
# find the bad numbers between them 
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

# given a length of str, return an array of that string's common factors
# i.e. len 10 returns [5,2,1]
def findLensToCheck(l):
    lens = []
    i = 1
    # print('testing length', l)
    while i < l: 
        if l % i == 0:
            lens.append(i)
        i += 1

    return lens

# checks cases, first by finding factors of the length of a string 
# then cut that str into equal lengths for each found factor 
# check that they are all equal, if they are equal, add them to our return arr,
# otherwise do nothing.
def checkCase(s):
    strlen = int(len(s))
    patternLens = findLensToCheck(strlen)
    badIds = []

    for subLen in patternLens:
        parts = [s[i:i + subLen] for i in range(0, len(s), subLen)] # split str into equal length
        # print(parts)
        equal = True

        # compare the start of the segment to the rest of it
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
res = 0
for i in badIds:
    res += i

print(res)
print('time', time.perf_counter() - startT)
# wow my solution is slow? 