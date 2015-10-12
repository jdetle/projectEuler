
numList = [1,2,3,4,5,6,7]
def product(numList):
    product = 1
    for i in range(len(numList)):
        product = product * numList[i]
    return product

print product(numList)
