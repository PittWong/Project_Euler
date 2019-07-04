# coding:utf-8


def get_divisors(num):
    divisors = [1]
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            divisors.append(divisor)
            if divisor != num / divisor:
                divisors.append(num / divisor)
    # print divisors
    return divisors


def is_abundant_num(num):
    divisors = get_divisors(num)
    sum_result = 0
    for divisor in divisors:
        sum_result += divisor
    if sum_result > num:
        return True
    return False


def get_all_abundant_less(num):

    all_abundants = []
    for sub_num in range(1, num + 1):
        if is_abundant_num(sub_num):
            all_abundants.append(sub_num)

    return all_abundants


# def get_all_abundant_sums(num):
#
#     all_abundants = get_all_abundant_less(num)
#     all_sums = []
#     num_count = len(all_abundants)
#     for index1 in range(1, num_count):
#         for index2 in range(index1, num_count):
#             num_sum = all_abundants[index1] + all_abundants[index2]
#             if num_sum > num:
#                 break
#
#             if num_sum not in all_sums:
#                 all_sums.append(num_sum)
#                 print num_sum
#
#     return all_sums



def get_all_abundant_sums(num):

    result = []
    all_abundants = get_all_abundant_less(num)
    for sub_num in range(1, num + 1):
        for abundant in all_abundants:
            if sub_num - abundant < abundant:
                break
            if sub_num - abundant in all_abundants:
                result.append(sub_num)
                print sub_num
                break
    return result


max_num = 28123
all_sums = 0
abundant_sums = get_all_abundant_sums(max_num)
for num in range(max_num + 1):
    if num not in abundant_sums:
        all_sums += num

print '最终结果是' + str(all_sums)

    # 最终结果是4179871
