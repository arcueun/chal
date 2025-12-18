# find the largest joltage with 12 numbers
def read_input():
    # with open("e3.txt", "r") as f:
    with open("3.txt", "r") as f:
        s = f.read().split()
        i = 0
        return s

# now we must account for 12 batteries 
def findLargestJolts(s):
    biggestJolts = s[:12]

    # 1-12 already exists, and we see 13 join us 
    # 2-13 
    # howeverm a number in the middle could be excluded, creating larger joltage
    # 1,3-13
    # 1-2,4-13
    # 1-3,5-13 
    # ...
    # 1-11,13 
    print(biggestJolts)
    print(len(biggestJolts))
    i = 12
    while i < len(s):
        j = 0 # position of current number to remove 
        
        while j < len(biggestJolts):
            newBiggest = biggestJolts[:j] + biggestJolts[j+1:] + s[i]
            # print('curNum:', biggestJolts, 'newNum:', biggestJolts[:j] + biggestJolts[j+1:] + s[i])

            if int(newBiggest) > int(biggestJolts):
                # print(newBiggest, 'is larger than', biggestJolts, 'the new num is', s[i], 'at pos j:', j)
                biggestJolts = newBiggest
                break
            j += 1

        i += 1

    return int(biggestJolts)
    
## main 
batteryRows = read_input()
totalPower = 0
for row in batteryRows:
    print(row, end=' ')
    totalPower += findLargestJolts(row)

print('total power:', totalPower)