
# A function that takes cuntless number of arguments to add

def add(*args):
    sum_ = 0
    for num in args:
        sum_ += num
    return sum_


print(add(2, 99, -5))
