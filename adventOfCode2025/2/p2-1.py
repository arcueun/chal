# read from file and present it as array of ranges
def parseInput():
    # with open("e2.txt", "r") as f:
    with open("2.wtxt", "r") as f:
        s = f.read().split(",")
        
        # for r in s:
        #     print(r) # ensure we split properly
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
            # print('test', i) # what num is this
            # print(len(str(i))) # check len of str 

            if len(str(i)) % 2 != 0:
                i += 1
                # print('odd num length')
                continue

            res = checkCase(str(i)) # check if number satisfies the case
            if res != 0:
                badNums.append(res)


            i += 1

    return badNums
            
# splits into front and half, checks if those halves are identical
def checkCase(s):
    strlen = int(len(s) / 2)
    frontHalf = s[strlen:]
    backHalf = s[:strlen]
    if frontHalf == backHalf: 
        print(s, 'is bad')
        return int(s)
    else:
        return 0
            
## main 
r = parseInput()
badIds = findBadIds(r)
print(badIds)
res = 0
for i in badIds:
    res += i

print(res)