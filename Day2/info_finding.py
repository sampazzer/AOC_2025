# Find the largest number so I know how many factors to work out for splitting the
# numbers when finding the patterns.

f = open("actual_input", "r")
ip = f.read().split(",")


def find_largest_digit_number(x):
    splitx = x.split("-")
    # returns the second number of the range as this will always be higher than the first
    return int(splitx[1])


num_store = 0
for nums in ip:
    compare_num = find_largest_digit_number(nums)
    if compare_num > num_store:
        num_store = compare_num
# prints the largest number
print(f"largest no: {num_store}")
# prints the digit length of that number
str_num_digit_length = len(str(num_store))
int_num_digit_length = int(str_num_digit_length)
# print(int_num_digit_length)

# get factors of numbers up to the largest digit number
for fnums in range(1, int_num_digit_length + 1):
    factors_of = []
    print(fnums)
    for ffnums in range(1, fnums + 1):
        # print(f"actualnum {fnums} / factor {ffnums}")
        if fnums % ffnums == 0:
            factors_of.append(ffnums)

    print(f"factors of {fnums}: {factors_of}")
