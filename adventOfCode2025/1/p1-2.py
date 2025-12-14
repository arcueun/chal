# read file 
lock = 50
pw = 0
# with open("e1.txt", "r") as f:
with open("1.txt", "r") as f:
    for line in f:
        print('lock =', lock)
        tmp = int(line[1:])
        if line[0] == 'R':
            lock += tmp
        else:
            if lock == 0:
                lock = 100
            lock -= tmp

        while lock < 0:
            lock += 100
            print('we\'re below 0, returning to range')
            pw += 1

        while lock >= 100:
            if lock == 100:
                lock = 0
                continue
            lock -= 100
            print('above 0, returning to range')
            pw += 1

        if lock == 0:
            print('ending with 0')
            pw += 1


print(lock, pw)

# add lockber to the value and add/subtract 100 on R / L operations respectively 
# if lockber exceeds 100, subtract/add 100 until it is [0, 99]