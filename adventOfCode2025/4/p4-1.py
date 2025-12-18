# read in the table of inputs 

def read_input():
    # recognise the length and the number of rows 
    inLength =-1
    inHeight =-1
    with open("e.txt", "r") as f:
    # with open("in.txt", "r") as f:
        s = f.read().split()
        inLength = len(s)
        for row in s:
            inHeight += 1
        i = 0

        print(s)
        print(inHeight, inLength)
        return s


#main 
read_input()