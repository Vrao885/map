

def my_func(n):
    return n*3

list1 = [1, 2, 3, 4, 5, 6, 7]

new_list= list(map(my_func, list1))
print(new_list)