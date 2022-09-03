def is_curzon(num):
    a = 2 * num + 1
    b = 2**5 + 1
    if b % a == 0:
        return True
    else:
        return False
result = is_curzon(6)
print(result)