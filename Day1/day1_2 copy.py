import math

i1 = "input1_1.txt"
i2 = "test_input.txt"
start = 50
zeroCount = 0
currentCount = 0
modulus = 100

f = open(i2, "r")
ip = f.read().splitlines()

currentCount = start
for i in ip:
    direction = i[0]
    amount = int(i[1:])
    print("currentCount: " + str(currentCount))
    if direction == "R":
        print("going right: " + str(amount))
        while amount != 0:
            whatsLeft = 99 - currentCount
            amount = amount - whatsLeft
            zeroCount +=1
            currentCount = 0

        currentCount = (currentCount + amount) % modulus

    elif direction == "L":
        print("going left: " + str(amount))
        currentCount = (currentCount - amount) % modulus

    print("afterCount: " + str(currentCount))
    print("zeroCount: " + str(zeroCount))


print("zeroCount: " + str(zeroCount))
