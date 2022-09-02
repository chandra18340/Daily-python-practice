def series_resistance(lst):
    i = 0
    rt = 0
    while i < len(lst):
        rt = rt + lst[i]
        i += 1
    else:
        if rt <=1:
            print(rt,"ohm")
        else:
            print(rt,"ohms")

series_resistance([1, 5, 6, 3])
