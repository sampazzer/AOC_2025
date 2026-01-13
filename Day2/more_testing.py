# def find_digit_len(num_for_digit):
#     str_dig_length = len(str(num_for_digit))
#     int_dig_length = int(str_dig_length)
#     return int_dig_length


def split_digits(num_to_be_split, f):
    str_num_split = str(num_to_be_split)
    chunks = [str_num_split[i : i + f] for i in range(0, len(str_num_split), f)]
    return chunks


# compares all the split up chunks, returns True if they are the same
def compare_chunks(chunk_list):
    res = all(chunk_list)
    return res


split_num = split_digits(121212, 2)
chunks_same = compare_chunks(split_num)
print(split_num)
print(chunks_same)
