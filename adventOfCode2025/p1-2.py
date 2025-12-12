# read file 
lock = 50
pw = 0
with open("eg.txt", "r") as f:
# with open("1.txt", "r") as f:
    for line in f:
        print('lock', lock)

        tamper = False
        if lock == 0 :
            print('!!!!!!!!!!!!~ starting at 0')
            pw += 1
            tamper = True
        
        tmp = int(line[1:])
        if line[0] == 'R':
            lock += tmp
        else:
            lock -= tmp

        while lock < 0:
            lock += 100
            print('inc pw on cross 0 case')
            if not tamper:
                pw += 1

        while lock >= 100:
            lock -= 100
            print('inc pw on cross 0 case')
            if not tamper:
                pw += 1



print(lock, pw)

# add lockber to the value and add/subtract 100 on R / L operations respectively 
# if lockber exceeds 100, subtract/add 100 until it is [0, 99]