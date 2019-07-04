# coding:utf-8


def get_max_without_high_place_num(place_count):

    max_kinds_without_high_place = 1
    for place in range(1, place_count):
        max_kinds_without_high_place *= place
    return max_kinds_without_high_place


def get_high_place_num_index(max_kinds_without_high_place, select_nums, target_index):
    for index in range(len(select_nums)):
        if (index + 1) * max_kinds_without_high_place > target_index:
            return index


def compute():

    place_count = 10
    select_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_index = 999999

    target_num = 0
    current_max_kinds = 0

    for place in range(place_count):
        max_kinds_without_high_place = get_max_without_high_place_num(place_count - place)
        print max_kinds_without_high_place

        target_index_num_index = get_high_place_num_index(max_kinds_without_high_place, select_nums, target_index - current_max_kinds)
        print '返回的index' + str(target_index_num_index)
        target_index_num = select_nums[target_index_num_index]

        target_num += target_index_num * 10 ** (place_count - place - 1)
        current_max_kinds += max_kinds_without_high_place * target_index_num_index

        # target_index -= current_max_kinds
        select_nums.remove(target_index_num)
        print '已经数过去的数量' + str(current_max_kinds)
        print target_num


    return target_num

print compute()
# 计算结果是2783915460