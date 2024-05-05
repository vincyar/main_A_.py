limit = int(input("Enter a number"))
i = 1
half = limit / 2
while i <= limit:
    j = 1

    while j <= i:
        print('*', end=" ")
        j = j + 1
    print()
    i = i + 1
