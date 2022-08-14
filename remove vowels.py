str = input("Enter any string: ")

vowels_string = ("aeiouAEIOU")

print("Input string",str)

for char in str:
    if char in vowels_string:
        str = str.replace(char,"")

print("output string without vowels",str)

