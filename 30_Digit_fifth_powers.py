# coding:utf-8


def compute():

    total = 0

    print 9 ** 5 * 10

    for num in range(2, 999999):
        powers_sum = 0
        for index in range(6, -1, -1):
            sub_num = num / (10 ** index) % 10
            powers_sum += sub_num ** 5

        if powers_sum == num:
            total += num
            print num

    print total

compute()
# 计算结果是 443839

