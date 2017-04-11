import random
list = []
for i in range(1, 100):
    list.insert (i, random.randrange(9999))
print ("Total items inserted into the list:" , len(list))
print("List values before sort: ", list)

def sortQuick(listArg):
    less = []
    equal = []
    greater = []
    if len(listArg) > 1:
        val = listArg[0]
        for x in listArg:
            if x < val:
                less.append(x)
            if x == val:
                equal.append(x)
            if x > val:
                greater.append(x)
        # + operator to join lists
        return sortQuick(less) + equal + sortQuick(greater)
    else:
        #when you only have one element in your listArg, just return the listArg.
        return listArg

print("List values after sort: ", sortQuick(list))
print("Least value in the list: ", sortQuick(list)[0])