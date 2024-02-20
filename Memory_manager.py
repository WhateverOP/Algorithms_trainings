def init_memory(max_n):
    memory = []
    for i in range(max_n):
        memory.append([0, i + 1, 0]) # [key, left son (used as a pointer on the next element in list), right son]
    return [memory, 0] # [memory list, pointer to the first availible (free) memory element]

def new_node(mem_struct):
    memory, first_free = mem_struct
    mem_struct[1] = memory[first_free][1]
    return first_free

def del_node(mem_struct, index):
    memory, first_free = mem_struct
    memory[index][1] = first_free
    mem_struct[1] = index