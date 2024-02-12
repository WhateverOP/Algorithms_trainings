def words_in_dict(dictionary, text):
    good_words = set(dictionary)
    for word in dictionary:
        for del_i in range(len(word)):
            good_words.add(word[:del_i] + word[del_i + 1:])
    ans = []
    for word in text:
        ans.append(word in good_words)
    return ans