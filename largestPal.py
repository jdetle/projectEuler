
products = []
counter = 0
check = '100001'
print len(check), check[0], check[len(check)-1]
def checkPal(num):
    palStr = str(num)
    for i in range(len(palStr)):
        if palStr[i] != palStr[len(palStr)-1-i]:
            #print "false", palStr[i]
            return False
    return True

print checkPal(999999)
print checkPal(10001)
print 999*999
greatestPal = 0
for i in range(100,1000):
    for j in range(100,1000):
        counter += 1
        if checkPal(i*j) and i*j>greatestPal:
            greatestPal = i*j

print greatestPal
