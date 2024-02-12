set_size = 10
my_set = [[] for i in range(set_size)]

def add(x):
    my_set[x % set_size].append(x)

def find(x):
    for now in my_set[x % set_size]:
        if now == x:
            return True
    return False

def delete(x):
    x_set_list = my_set[x % set_size]
    for i in range(len(x_set_list)):
        if x_set_list[i] == x:
            x_set_list[i], x_set_list[len(x_set_list) - 1] = x_set_list[len(x_set_list) - 1], x_set_list[i]
            x_set_list.pop()
            return