def double_letters(letters):
    for letter in range(len(letters)-1):
        if letters[letter] == letters[letter+1]:
            return True
    return False

print(double_letters("letters"))