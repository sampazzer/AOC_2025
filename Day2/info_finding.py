# Find the largest number so I know how many factors to work out for splitting the
# numbers when finding the patterns.

f = open("actual_input", "r")
ip = f.read().split(",")


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


# text = "ABCDEFGH"
# n = 2
# chunks = [text[i:i+n] for i in range(0, len(text), n)]

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
    print(fnums)
    factors_of_temp = []
    for ffnums in range(1, fnums + 1):
        # print(f"actualnum {fnums} / factor {ffnums}")
        if fnums % ffnums == 0:
            factors_of_temp.append(ffnums)
    factors_of_perm.append(factors_of_temp)

print(f"factors of {fnums}: {factors_of_perm}")

# UP TO THIS POINT I HAVE A LARGEST DIGIT NUMBER AND ALL THE FACTORS UP TO AND
# INCLUDING THAT DIGIT NUMBER E.G. 52355 LARGEST DIGIT WOULD BE 5, I HAVE ALL
# FACTORS OF NUMBERS 1 THROUGH 5
# factors_of_perm = all the factors of each digit number
