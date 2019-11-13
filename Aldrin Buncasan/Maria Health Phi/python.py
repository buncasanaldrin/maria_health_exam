x = 0
previous_number = 1
range_number = 100000
while x < range_number:
    if x % 3 == 0:
        print('Maria Health' if x % 5 == 0 else 'Maria')
    elif x % 5 == 0:
        print('Health')
    else:
        print(x)

    x = (x + previous_number)
    previous_number = (x - previous_number)
