import timeit


def listitems(lis):
    del (lis[9])
    return lis


def time_taken(n):
    start_time = timeit.timeit()
    result = listitems(n)
    end_time = timeit.timeit()
    return end_time - start_time, result


print time_taken(listitems([1, 2, 3, 4, 5, 6, 5, 4, 8, 7, 6, 9, 45, 4, 6, 2, 12, [1, 5, 8, 9, 4, 54]]))


def dictionary(dic):
    del (dic['Topic'])
    return dic


def time_taken(n):
    start_time = timeit.timeit()
    result = n
    end_time = timeit.timeit()
    return end_time - start_time, result


print time_taken(dictionary({'Name': 'Babita', ' Age': 23, 'Learning': 'Python', 'Topic': 'Big O Notation'}))
