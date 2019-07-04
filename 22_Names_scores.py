# coding:utf-8

alphabetMap = dict()


def get_alphabet_score(char):
    if len(alphabetMap) == 0:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for alphabet in alphabets:
            alphabetMap[alphabet] = len(alphabetMap) + 1

        print(alphabetMap)

    one_alphabet = char.lower()

    return alphabetMap[one_alphabet]


def get_name_score(name):
    lower_name = name.lower()
    name_score = 0
    for alphabet in lower_name:
        name_score += get_alphabet_score(alphabet)

    return name_score


def name_cmp(name1, name2):
    less_len = min(len(name1), len(name2))

    # print name1 + '  ' + name2
    for index in range(0, less_len):
        alphabet1 = name1[index]
        alphabet2 = name2[index]
        # print alphabet1 + ' ' + alphabet2
        score1 = get_alphabet_score(alphabet1)
        score2 = get_alphabet_score(alphabet2)

        # print str(score1) + ' ' + str(score2)

        if score1 > score2:
            return 1
        if score1 < score2:
            return -1
        continue
    return -1 if len(name1) < len(name2) else 1


def get_names(names_file):
    fo = open(names_file, 'r')
    names = fo.read()
    names = names.replace('\"', '')
    fo.close()
    name_list = names.split(',')
    print name_list
    print len(name_list)

    name_list.sort()

    all_score = 0
    for index in range(0, len(name_list)):
        name_score = get_name_score(name_list[index])
        all_score += name_score * (index + 1)
        print name_list[index] + ' ' + str(index + 1) + ' ' + str(name_score)

    print(all_score)

    temp = 871198282 - all_score
    # temp = temp / 6164
    print(temp)

    print name_list
    print len(name_list)


get_names('p022_names.txt')
# 最终结果是871198282
