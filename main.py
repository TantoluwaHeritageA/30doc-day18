import string


def rev_str(word):
    words = []
    punc = {}
    new_word = ''
    print(word)
    words = word.split(' ')
    for i in words:
        if i[-1] in string.punctuation:
            p = i[-1]
            punc[p] = words.index(i)
            words[words.index(i)] = i[: -1]
    punc_list = list(punc.values())
    punc_keys = list(punc.keys())
    num = 0
    for i in range(0, len(punc_list)):
        index = -(i+1)
        position = punc_list.index(punc_list[i])
        key = punc_keys[position]
        if i != len(punc_list)-1:
            num = num + punc_list[index] - punc_list[index-1]
        else:
            num = punc_list[i] + 1
        punc[key] = num
    punc_list = list(punc.values())
    punc_keys = list(punc.keys())

    for w in range(0, len(words)):
        if w+1 in punc.values():
            position = punc_list.index(w+1)
            key = punc_keys[position]
            x = - (w+1)
            new_word = new_word + words[x] + key + " "
        else:
            x = - (w+1)
            new_word = new_word + words[x] + " "

    print(new_word)
