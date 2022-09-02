def factorial(num):
    result = 1
    limit = num
    while limit > 0:
        for i in range (1, num + 1):
            result = result * i
            limit = limit - 1
            print(result)

factorial(3)