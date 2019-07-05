# coding:utf-8


def get_cycles_num(num, divisor):

    remainders = []
    sub_num_remainder_map = {}
    current_remainder = num

    while current_remainder not in remainders:
        remainders.append(current_remainder)
        current_remainder *= 10
        if current_remainder < divisor:
            sub_num_remainder_map[current_remainder / 10] = 0
        else:
            sub_num_remainder_map[current_remainder / 10] = current_remainder / divisor
            current_remainder = current_remainder % divisor

    cycles = []
    begin = False
    for remainder in remainders:
        if remainder == current_remainder:
            begin = True

        if begin:
            cycles.append(sub_num_remainder_map[remainder])

    return cycles


def compute():
    max_length = 0
    max_length_cycles = []
    for num in range(1, 1000):
        cycles = get_cycles_num(1, num)
        if len(cycles) > max_length:
            max_length = len(cycles)
            max_length_cycles = cycles
            print max_length_cycles
            print '当前num为' + str(num)

    print max_length_cycles


compute()
# 计算结果为983

