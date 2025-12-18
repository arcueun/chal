# from list of valid ids and a list of ids (list B)
# determine which listBIds are valid. 

def read_input():
    # collect valid ids until blank
    with open("e.txt", "r") as f:
    # with open("in.txt", "r") as f:
        s = f.read().split("\n")
        validIdArr = []
        for row in s:
            validIdArr.append(row)
            if len(row) == 0:
                break

        productIdArr = []
        for row in s:
            productIdArr.append(row)

        return validIdArr, productIdArr


#main 
validId, productId = read_input()
print(validId)
print(productId)
#TODO validId list so it is numerical