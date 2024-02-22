'''
Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки abcaabdddettq равна 3)

Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций замены символа. 

Формат ввода

В первой строке записано одно целое число k (0 ≤ k ≤ 109)

Во второй строке дана непустая строчка S (|S| ≤ 2 ⋅ 105). Строчка S состоит только из маленьких латинских букв. 

Формат вывода

Выведите одно число — максимально возможную красоту строчки, которую можно получить. 
'''

path_to_text = "/home/opv002/py_notes/git_repos/Algorithms_trainings/trainings_3_division_B/data/Beautiful_string_2_text_2.txt"
text = open(path_to_text)

l_input = []
for string in text:
    if string == '\n':
        continue
    string = string.replace('\n','')
    l_input.append(string)

k = int(l_input[0])
S = l_input[1]