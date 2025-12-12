# read file 
num = 50
pw = 0
# with open("eg.txt", "r") as f:
with open("1.txt", "r") as f:
    for line in f:
        tmp = int(line[1:])
        if line[0] == 'R':
            num += tmp
        else:
            num -= tmp

        while num < 0:
            num += 100
        
        while num >= 100:
            num -= 100
    
        if num == 0:
            pw += 1
        print('num', num)

print(num, pw)

# add number to the value and add/subtract 100 on R / L operations respectively 
# if number exceeds 100, subtract/add 100 until it is [0, 99]
# ans = 1172