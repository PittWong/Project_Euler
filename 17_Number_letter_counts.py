# coding:utf-8

def get_num_string_less20(num):

    if num >= 20 :
        return '';
    num_strings = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'];

    return num_strings[num];


def get_num_string_tensplace(num):
    index = num / 10;
    tensplaceStrings = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'];
    return tensplaceStrings[index];


def get_num_string(num):

    if num < 20 :
        return get_num_string_less20(num)

    hundred_place_num = num / 100;
    hundred_place_str = get_num_string_less20(hundred_place_num) + ' hundred' if (hundred_place_num > 0) else ''



    if num % 100 < 20:
        tens_byte_place_str = get_num_string_less20(num % 100);
    else:
        tens_place_str = get_num_string_tensplace(num % 100);
        byte_place_str = get_num_string_less20(num % 10);

        tens_byte_place_str = tens_place_str + ' ' + byte_place_str;

    return hundred_place_str + (' and ' if (len(hundred_place_str) > 0 and len(tens_byte_place_str) > 0) else '') + tens_byte_place_str;


def number_letter_counts():
    total_count = 0
    for num in range(1,1000):
        num_string = get_num_string(num)
        print num_string + ' ' + str(num)
        num_string = num_string.replace(' ','')
        count = len(num_string)
        total_count += count;
        print count

    total_count += len('onethousand')
    print(total_count)


number_letter_counts()
# 计算结果是21124
