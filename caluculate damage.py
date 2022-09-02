from pickletools import read_string1


def damage(damage, speed, time):
   a = damage * speed
   if a < 0:
    return "invalid" 
   elif time == "second":
    return a * 3600
   elif time == "minute":
    return a * 60
   elif time == "hour":
    return a
result = damage(2, 2, "second")
print(result)