# Notes
"""
If 3487 is the number and your looking for a pattern then the last digit in the pattern
needs to match the last digit in the whole number for the pattern e.g. looking for pattern
34 then we know its not a pattern because the last digit is a 7 therefore move on
"""

f = open("practice_input", "r")
ip = f.read().split(",")

# empty array for putting in the numbers with patterns
pattern_array = []

print(ip)


# takes a string and will check for patterns
def figure_range(x):
    splitx = x.split("-")

    print(splitx[0])
    print(len(splitx))


figure_range(ip[0])
