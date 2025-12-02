start = 50
zeroCount = 0
currentCount = 0
modulus = 100

f = open("input1_1.txt", "r")
ip = f.read().splitlines()

currentCount = start
for i in ip:
    direction = i[0]
    amount = int(i[1:])
    if direction == "R":
        currentCount = (currentCount + amount) % modulus
    elif direction == "L":
        currentCount = (currentCount - amount) % modulus
    if currentCount == 0:
        zeroCount += 1

print(zeroCount)
