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
        if currentCount + amount > modulus and currentCount != 0:
            newNum = math.floor(amount / modulus)
            if newNum == 0:
                zeroCount += 1
            if newNum > 0 and (currentCount + amount) % modulus != 0:
                zeroCount = zeroCount + newNum
            if newNum > 0 and (currentCount + amount) % modulus == 0:
                zeroCount = zeroCount + newNum + 1
        elif currentCount == 0 and amount >= modulus:
            newNum = math.floor(amount / modulus)
            if newNum == 0:
                zeroCount += 1
            elif newNum > 0:
                zeroCount = zeroCount + newNum
        if (
            (currentCount + amount) % modulus == 0
            and currentCount != 0
            and amount < modulus
        ):
            zeroCount += 1
        currentCount = (currentCount + amount) % modulus

    elif direction == "L":
        print("going left: " + str(amount))
        if currentCount - amount < 0 and currentCount != 0:
            newNum = math.floor((abs(amount)) / modulus)
            if newNum == 0:
                zeroCount += 1
            if newNum > 0 and (currentCount - amount) % modulus != 0:
                zeroCount = zeroCount + newNum
            if newNum > 0 and (currentCount - amount) % modulus == 0:
                zeroCount = zeroCount + newNum + 1
        elif currentCount == 0 and amount >= modulus:
            newNum = math.floor((abs(amount)) / modulus)
            if newNum == 0:
                zeroCount += 1
            elif newNum > 0:
                zeroCount = zeroCount + newNum
        if (
            (currentCount - amount) % modulus == 0
            and currentCount != 0
            and amount < modulus
        ):
            zeroCount += 1
        currentCount = (currentCount - amount) % modulus

    print("afterCount: " + str(currentCount))
    print("zeroCount: " + str(zeroCount))


print("zeroCount: " + str(zeroCount))
