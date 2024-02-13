s = input()
s_splitted = s.split(' ')

def group_words(words):
    groups_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in groups_dict:
            groups_dict[sorted_word] = []
        groups_dict[sorted_word].append(word)
    ans = []
    for sorted_word in groups_dict:
        ans.append(groups_dict[sorted_word])
    return ans

print(group_words(s_splitted))