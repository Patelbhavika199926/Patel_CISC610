import time
dict = {}
t_st = time.time()
for i in range(1, 50000):
    dict.update({str(i): i})
t_end = time.time()
print("Total items inserted in the Dictionary: ", len(dict))
print ("Time taken to insert values in Dict:", t_end - t_st)

t_st = time.time()
for i in range(1, 50000):
    dict.get(i)
t_end = time.time()
print ("Time taken to get values from Dict:", t_end - t_st)