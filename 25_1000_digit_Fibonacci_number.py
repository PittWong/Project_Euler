# coding:utf-8


def fibonacci():

    num_f1 = 1
    num_f2 = 1
    n = 2

    target_num = 10 ** 999
    print target_num
    while num_f2 < target_num:
        n += 1
        temp = num_f2
        num_f2 = num_f1 + num_f2
        num_f1 = temp

    print n

fibonacci()
# 结果是 4782 (python算这个题有点取巧,没有位数限制)