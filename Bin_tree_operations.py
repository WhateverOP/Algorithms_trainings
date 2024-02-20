def find(mem_struct, root, x):
    key = mem_struct[0][root][0]
    if x == key:
        return root
    elif x < key:
        left = mem_struct[0][root][1]
        if left == -1:
            return -1
        else:
            return find(mem_struct, left, x)
    elif x > key:
        right = mem_struct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(mem_struct, right, x)
        
def create_and_fill_node(mem_struct, key):
    index = new_node(mem_struct)
    mem_struct[0][root][0] = key
    mem_struct[0][root][1] = -1
    mem_struct[0][root][2] = -1
    return index

# def add(mem_struct, root, x):
