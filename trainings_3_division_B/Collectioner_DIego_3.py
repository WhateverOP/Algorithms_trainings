'''
Диего увлекается коллекционированием наклеек. На каждой из них написано число, и каждый коллекционер мечтает собрать наклейки со всеми встречающимися числами.

Диего собрал N наклеек, некоторые из которых, возможно, совпадают.
Как-то раз к нему пришли K коллекционеров. i-й из них собрал все наклейки с номерами не меньшими, чем pi.
Напишите программу, которая поможет каждому из коллекционеров определить, сколько недостающих ему наклеек есть у Диего. Разумеется, гостей Диего не интересуют повторные экземпляры наклеек.

Формат ввода

В первой строке содержится единственное число N (0 ≤ N ≤ 100 000) — количество наклеек у Диего.
В следующей строке содержатся N целых неотрицательных чисел (не обязательно различных) — номера наклеек Диего. Все номера наклеек не превосходят 109.
В следующей строке содержится число K (0 ≤ K ≤ 100 000) — количество коллекционеров, пришедших к Диего.
В следующей строке содержатся K целых чисел pi (0 ≤ pi ≤ 109), где pi — наименьший номер наклейки, не интересующий i-го коллекционера.

Формат вывода

Для каждого коллекционера в отдельной строке выведите количество различных чисел на наклейках, которые есть у Диего, но нет у этого коллекционера. 
'''

import random

path_to_text = "/home/opv002/py_notes/git_repos/Algorithms_trainings/trainings_3_division_B/data/Collectioner_Diego_3_text_1.txt"
# path_to_text = "/home/opv002/py_notes/git_repos/Algorithms_trainings/trainings_3_division_B/data/Collectioner_Diego_3_text_2.txt"
# path_to_text = "/home/opv002/py_notes/git_repos/Algorithms_trainings/trainings_3_division_B/data/Collectioner_Diego_3_text_3.txt"
text = open(path_to_text)

lines = []
for line in text.readlines():
    if line == '\n':
        continue
    line = line.replace('\n', '')
    lines.append(line)

N = int(lines[0])
N_arr = [int(i) for i in lines[1].split(' ')]    # это массив из N номеров, которые есть у Диего НОМЕРА МОГУТ ПОВТОРЯТЬСЯ
K = int(lines[2])
K_arr = [int(i) for i in lines[3].split(' ')]    # это массив из K номеров, ВСЕ номера МЕНЬШЕ этих интересуют k-ого коллекционера

def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l

def r_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, check_params):
            l = m
        else:
            r = m - 1
    return l

def check_is_l(index, params):
    seq, x = params
    return seq[index] < x

def get_number_of_stickers_better(N_arr, K_arr):
    N_arr_copy = N_arr.copy()
    N_arr_unique = list(set(N_arr_copy))
    N_arr_sorted_unique = sorted(N_arr_unique)
    K_arr_interesting = [0] * len(K_arr)
    for i in range(0, len(K_arr)):
        if len(N_arr_sorted_unique) == 1:
            if N_arr_sorted_unique[0] < K_arr[i]:
                K_arr_interesting[i] = 1
            else:
                K_arr_interesting[i] = 0
        else:
            index = r_bin_search(0, len(N_arr_sorted_unique) - 1, check_is_l, (N_arr_sorted_unique, K_arr[i]))
            if index == 0 and N_arr_sorted_unique[index] >= K_arr[i]:
                K_arr_interesting[i] = 0  
            else:
                K_arr_interesting[i] = len(N_arr_sorted_unique[0:index + 1])
    return K_arr_interesting



def get_number_of_stickers_slow(N_arr, K_arr):
    N_arr_copy = N_arr.copy()
    N_arr_unique = list(set(N_arr_copy))
    N_arr_sorted_unique = sorted(N_arr_unique)
    K_arr_interesting = [0] * len(K_arr)
    for i in range(0, len(K_arr)):
        j_max = 0
        for j in range(len(N_arr_sorted_unique) - 1, -1, -1):
            if N_arr_sorted_unique[j] < K_arr[i]:
                j_max = j + 1
                break
        K_arr_interesting[i] = len(N_arr_sorted_unique[0:j_max])
    return K_arr_interesting


def get_number_of_stickers_better(N_arr, K_arr):
    N_arr_copy = N_arr.copy()
    N_arr_unique = list(set(N_arr_copy))
    N_arr_sorted_unique = sorted(N_arr_unique)
    K_arr_interesting = [0] * len(K_arr)
    
    # N_arr_sorted = sorted(N_arr)
    # N_arr_sorted_unique = []
    # N_arr_sorted_unique.append(N_arr_sorted[0])
    # for i in range(0, len(N_arr_sorted)):
    #     if N_arr_sorted_unique[-1] != N_arr_sorted[i]:
    #         N_arr_sorted_unique.append(N_arr_sorted[i])
    return N_arr_sorted_unique

N_arr = [1, 2, 3, 1, 3, 9, 1, 5] 
K_arr = [1, 8, 2] 

# ans = get_number_of_stickers_slow(N_arr, K_arr)
# ans = get_number_of_stickers_better(N_arr, K_arr)
ans = get_number_of_stickers_better(N_arr, K_arr)
for i in ans:
    print(i)

# N_arr = [1, 9, 5] 
# K_arr = [1, 8, 2] 

# N_arr = [10, 7, 5] 
# K_arr = [9, 10, 2]

# N_arr = [9, 5, 7] 
# K_arr = [0, 10, 7] 

# ans_better = get_number_of_stickers_better(N_arr, K_arr)
# print('ans better:')
# for i in ans_better:
#     print(i)

# ans_slow = get_number_of_stickers_slow(N_arr, K_arr)
# print('ans slow:')
# for i in ans_slow:
#     print(i)

# while True:
#     N_arr = [random.randint(0, 1e1) for i in range(3)]
#     K_arr = [random.randint(0, 1e1) for i in range(3)]
#     ans_slow = get_number_of_stickers_slow(N_arr, K_arr)
#     ans_better = get_number_of_stickers_better(N_arr, K_arr)
#     if (ans_slow == ans_better):
#         print(f'OK: \n N_arr = {N_arr} \n K_arr = {K_arr} \n ans_slow = {ans_slow} -> {ans_slow} == {ans_better}')
#     else:
#         print(f'NOT OK: \n N_arr = {N_arr} \n K_arr = {K_arr} \n ans_slow = {ans_slow} -> {ans_slow} != {ans_better}')
#         break
        