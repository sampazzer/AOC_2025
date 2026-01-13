# Find the largest number so I know how many factors to work out for splitting the
# numbers when finding the patterns.

f = open("practice_input", "r")
ip = f.read().split(",")


# FUNCTIONS
# get second number in the range
def find_largest_digit_number(x):
    splitx = x.split("-")
    # returns the second number of the range as this will always be higher than the first
    return int(splitx[1])


# returns digit length of number
def find_digit_len(num_for_digit):
    str_dig_length = len(str(num_for_digit))
    int_dig_length = int(str_dig_length)
    return int_dig_length


# want to split the number into its component digits depending on its divisible factor
# it takes in the number, the factor and returns a list of the split up value
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
            # breaks if the element next to it isnt the same
            res = False
            break
        count += 1
    return res


# FIRST OPERATION
# finding largest number and finding how many digits it is
num_store = 0
for nums in ip:
    compare_num = find_largest_digit_number(nums)
    if compare_num > num_store:
        num_store = compare_num
# prints the largest number
print(f"largest no: {num_store}")
str_num_digit_length = len(str(num_store))
int_num_digit_length = int(str_num_digit_length)

# get factors of numbers up to the largest digit number
# factors of perm will be the factors of a number going up from 1 (it is indexed to 0)
factors_of_perm = []
for fnums in range(1, int_num_digit_length + 1):
    print(f"fnums: {fnums}")
    factors_of_temp = []
    for ffnums in range(1, fnums + 1):
        print(f"ffnums: {ffnums}")
        # print(f"actualnum {fnums} / factor {ffnums}")
        if fnums % ffnums == 0:
            factors_of_temp.append(ffnums)
    factors_of_perm.append(factors_of_temp)

print(f"factors: {factors_of_perm}")

# UP TO THIS POINT I HAVE A LARGEST DIGIT NUMBER AND ALL THE FACTORS UP TO AND
# INCLUDING THAT DIGIT NUMBER E.G. 52355 LARGEST DIGIT WOULD BE 5, I HAVE ALL
# FACTORS OF NUMBERS 1 THROUGH 5
# factors_of_perm = all the factors of each digit number

# SECOND OPERATION
"""
TODO:
[x] If we have single digit numbers, it may pass because the list only has 1 thing to compare with all()
I assume single digits are not patterns.
[ ] Factors dont want to include the top factor because then its not a pattern as its not split at all.
I think i actually handle this by accident in my compare_chunks function as any chunk list that only has 1
entry is rejected, this means that a 10 digit number split by factor of 10 would be only one element long
and fail in compare_chunks anyway.
"""
valid_ids = []
# taking each range from the input text e.g. 11-22
for nums in ip:
    split_range = nums.split("-")
    print(split_range)
    # taking each number in that range e.g. if range was 1-10 this will loop with numbers 1,2,3,4,5,6,7,8,9,10
    for range_nums in range(int(split_range[0]), int(split_range[1]) + 1):
        print(f"number for test: {range_nums}")
        # need to now take each num and do a for loop for how many factors its digits are divisible by
        # and compare the split lists
        # valid_ids is the list of valid id's
        # range_nums is the numbers im testing
        # num_len is the digit length of that number
        # factor is the factor im testing for
        num_len = find_digit_len(range_nums)
        for factor in factors_of_perm[num_len - 1]:
            valid = True
            print(f"testing factor: {factor}")
            dig_pattern = split_digits(range_nums, factor)
            print(f"dig pattern: {dig_pattern}")
            check_for_pattern = compare_chunks(dig_pattern)
            if check_for_pattern:
                valid = False
                break
        if valid:
            valid_ids.append(range_nums)
print(f"valid id's: {valid_ids}")
print(f"sum of id's: {sum()}")
