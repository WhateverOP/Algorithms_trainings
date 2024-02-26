def push_heap(heap_list, x):
    heap_list.append(x)
    pos = len(heap_list) - 1
    while pos > 0 and heap_list[pos] < heap_list[(pos - 1) // 2]:
        heap_list[pos], heap_list[(pos - 1) // 2] = heap_list[(pos - 1) // 2], heap_list[pos]
        pos = (pos - 1) // 2

def pop_heap(heap_list):
    ans = heap_list[0]
    heap_list[0] = heap_list[-1]
    pos = 0
    while pos * 2 + 2 < len(heap_list):   # while right son is in the heap
        min_son_index = pos * 2 + 1       # index of the left son
        if heap_list[pos * 2 + 2] < heap_list[min_son_index]:   # if the right son is less then left son -> swap
            min_son_index = pos * 2 + 2
        if heap_list[pos] > heap_list[min_son_index]:
            heap_list[pos], heap_list[min_son_index] = heap_list[min_son_index], heap_list[pos]
            pos = min_son_index
        else:
            break
    heap_list.pop()
    return ans