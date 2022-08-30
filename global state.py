balance = 8000

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdrawn(amount):
    global balance
    balance -= amount
    return balance

result1 = deposit(1000)
result2 = withdrawn(2000)
print(result1)
print(result2)