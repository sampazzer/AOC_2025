# def find_digit_len(num_for_digit):
#     str_dig_length = len(str(num_for_digit))
#     int_dig_length = int(str_dig_length)
#     return int_dig_length


def split_digits(num_to_be_split, f):
    str_num_split = str(num_to_be_split)
    chunks = [str_num_split[i : i + f] for i in range(0, len(str_num_split), f)]
    return chunks


# compares all the split up chunks, returns True if they are the same
# it loops only until the second the last one as we dont need to compare the last one with anything
def compare_chunks(chunk_list):
    # this is for indexing and comparing the chunk next to the one in the for loop
    count = 1
    res = False
    # if its only a single digit full number e.g. the chunk_list is only 1, then it doesnt even enter the for loop
    # and returns false which is what we want.
    for num in range(len(chunk_list) - 1):
        chunk = chunk_list[num]
        print(len(chunk))
        if chunk == chunk_list[count]:
            res = True
        else:
            res = False
            break
        count += 1
    return res


split_num = split_digits(22, 2)
chunks_same = compare_chunks(split_num)
print(split_num)
print(chunks_same)
