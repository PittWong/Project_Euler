# coding:utf-8


def compute():

    cycle_count = 1
    curent_num = 1
    total = 1
    edge = cycle_count * 2 + 1

    while edge <= 1001:
        for i in range(4):
            curent_num += edge - 1
            total += curent_num
            print curent_num
        cycle_count += 1
        edge = cycle_count * 2 + 1

    print total


compute()
# 计算结果是669171001