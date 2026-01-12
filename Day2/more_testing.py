# def find_digit_len(num_for_digit):
#     str_dig_length = len(str(num_for_digit))
#     int_dig_length = int(str_dig_length)
#     return int_dig_length


def split_digits(num_to_be_split, f):
    str_num_split = str(num_to_be_split)
    chunks = [str_num_split[i : i + f] for i in range(0, len(str_num_split), f)]
    return chunks


split_num = split_digits(223344, 2)
print(split_num)
