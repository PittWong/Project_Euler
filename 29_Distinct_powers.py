# coding:utf-8


def compute():

    terms = []
    for i in range(2, 100 + 1):
        for j in range(2, 100 + 1):
            if i ** j not in terms:
                terms.append(i ** j)
    print terms
    print len(terms)


compute()
# 计算结果为9183
