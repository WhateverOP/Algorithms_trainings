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


path_to_text = "/home/opv002/py_notes/git_repos/Algorithms_trainings/trainings_3_division_B/data/Collectioner_Diego_3_text_1.txt"
# path_to_text = "/home/opv002/py_notes/git_repos/Algorithms_trainings/trainings_3_division_B/data/Collectioner_Diego_3_text_2.txt"
text = open(path_to_text)

lines = []
for line in text.readlines():
    if line == '\n':
        continue
    line = line.replace('\n', '')
    lines.append(line)

N = int(lines[0])
N_arr = [int(i) for i in lines[1].split(' ')]
K = int(lines[2])
K_arr = [int(i) for i in lines[3].split(' ')]
# print(N, N_arr, K, K_arr)

def get_number_of_stickers(N_arr, K_arr):
    N_arr_sorted = sorted(N_arr)
    K_arr_interesting = [] # *len(K_arr)
    # print(N_arr_sorted)
    for i in range(0, len(K_arr)):
        j_max = 0
        for j in range(len(N_arr_sorted) - 1, -1, -1):
            # print(f'N_arr_sorted[{j}] = {N_arr_sorted[j]}')
            if N_arr_sorted[j] < K_arr[i]:
                j_max = j + 1
                break
        # K_arr_interesting.append(N_arr_sorted[0:j_max])
        K_arr_interesting.append(len(N_arr_sorted[0:j_max]))
    return K_arr_interesting

ans = get_number_of_stickers(N_arr, K_arr)
for i in ans:
    print(i)
        