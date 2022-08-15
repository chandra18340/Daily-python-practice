txt = input("Enter any sentance:  ").split(" ")

a = 0
index = ''

for i in txt:
    if len(i) > a:
        a = len(i)
        index = i
print(index)