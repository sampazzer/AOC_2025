i1 = "input1_1.txt"
i2 = "test_input.txt"
start = 50
zeroCount = 0
currentCount = 0
modulus = 100
f = open(i1, "r")
ip = f.read().splitlines()

# current count is set to the start amount(50) for the first run
currentCount = start
for i in ip:
    # left or right?
    direction = i[0]
    # how many clicks left or right?
    amount = int(i[1:])
    # get the current location
    print("NEW currentCount: " + str(currentCount))

    # going right
    if direction == "R":
        print("going right: " + str(amount))
        # find out if it is even going to reach 0
        # if it reaches 100, that means that it will go to or past 0
        # difference from current count to 100
        difference = 100 - currentCount
        if amount < difference:
            print("going to just do the calc")

        elif amount >= difference:
            changeAmount = amount
            while changeAmount >= difference:
                # if we get here we know to count up
                zeroCount += 1
                # this puts us to position 0
                changeAmount = changeAmount - difference
                # were only now really bothered if theres another 100 to trigger the 0 again
                difference = 100

        currentCount = (currentCount + amount) % modulus

    # going left
    elif direction == "L":
        print("going left: " + str(amount))
        # find out if theres even enough to go left to 0
        # if were starting at 0 then the difference isnt 0 because we have to go left another 100 to get back to 0
        if currentCount == 0:
            difference = 100
        else:
            difference = currentCount
        if amount < difference:
            print("going to just do the calc")

        elif amount >= difference:
            changeAmount = amount
            while changeAmount >= difference:
                # if we get here we know to count up
                zeroCount += 1
                changeAmount = changeAmount - difference
                # were only now really bothered if theres another 100 to trigger the 0 again
                difference = 100
                print(f"new changeamount: {changeAmount}")

        currentCount = (currentCount - amount) % modulus

    print("afterCount: " + str(currentCount))
    print("zeroCount: " + str(zeroCount))
    print("")


print("zeroCount: " + str(zeroCount))
