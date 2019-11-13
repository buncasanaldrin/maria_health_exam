# x will be the fibonacci sequence number of every loop
x = 0
# prev_number is the number we will use to know the previous number of fibonacci sequence
prev_number = 1
# range_number number range we will use for the fibonacci sequence
range_number = 100000
while x < range_number:

    # check if x is multiple of 3
    if x % 3 == 0:
        # print Maria Health if x is multiple of 5. else, print Maria
        print('Maria Health' if x % 5 == 0 else 'Maria')

    # check if x is multiple of 5 only
    elif x % 5 == 0:
        print('Health')

    # if not multiple of 3 or 5, 3 and 5, it will just return the fibonacci numbers
    else:
        print(x)

    # add the previous and current number to get the fibonacci sequence
    x = (x + prev_number)

    # set the previous number
    prev_number = (x - prev_number)

