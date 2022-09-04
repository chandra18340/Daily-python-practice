def mood_today(mood):
    if mood == None:
        return "Today, I am feeling neutral"
    else:
        return "Today, I am feeling  " + mood

result = mood_today("Happy")
print(result)