def end_corona(recovers, new_cases, active_cases):
    ac = active_cases
    count = 0
    while ac > 0:
        ac -= active_cases - recovers + new_cases
        count += 1
    if ac == 0:
        return count 

result = end_corona(100, 30, 500)
print(result)