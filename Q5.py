import random
list = []
upperLimit = 100
for i in range(1, upperLimit):
    list.insert (i, random.randrange(9999))
print ("Total items inserted into the list:" , len(list))
leastVal = list[0]
for i in range(1, upperLimit - 1):
    if list[i] < leastVal:
        leastVal = list[i]

print("Least value in the list: ", leastVal)