# coding:utf-8


primes_pool = []
no_primes_pool = []


def is_primes_number(num):

    if num < 2:
        return False
    if num in primes_pool:
        return True
    if num in no_primes_pool:
        return False


    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            no_primes_pool.append(num)
            return False

    primes_pool.append(num)
    return True


def compute():

    max_n = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            # print '当前n' + str(n) + ',--a,b分别是' + str(a) + ',' + str(b)
            while is_primes_number(n*n + n * a + b):
                n += 1
            if max_n < n:
                max_n = n
                print '当前最大的n是' + str(max_n) + ',--a,b分别是' + str(a) + ',' + str(b) + ',--乘积为' + str(a * b)

    # for a in range(-79, -78):
    #     for b in range(1601, 1602):
    #         n = 0
    #         print '当前n' + str(n) + ',--a,b分别是' + str(a) + ',' + str(b)
    #         while is_primes_number(n*n + n * a + b):
    #             n += 1
    #         if max_n < n:
    #             max_n = n
    #             print '当前最大的n是' + str(max_n) + ',--a,b分别是' + str(a) + ',' + str(b) + ',--乘积为' + str(a * b)

    print max_n


compute()
# 计算结果为983
