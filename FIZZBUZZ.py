n = []
for i in range(0,50):
    if (i % 3) and (i % 5) == 0:
        print("FIZZBUZZ")
    elif (i % 3) == 0:
        print("FIZZ")
    elif (i % 5) == 0:
        print("BUZZ")
