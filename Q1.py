import timeit
import random

for i in range(1000, 20000, 3000):
    t = timeit.Timer("x.index(random.randrange(%d))"%i,
                     "from __main__ import random, x")

    x = list(range(i))
    indextime = t.timeit(number=1000)
    print("%d, %15.5f" %(i, indextime))