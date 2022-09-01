def calculator(num1, operator, num2):
    if operator == "/" and num2 == 0:
        return  "can't divided by Zero !"
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2

    if operator == "/":
        return num1 / num2

result = calculator(2, "+", 2)
print(result)
