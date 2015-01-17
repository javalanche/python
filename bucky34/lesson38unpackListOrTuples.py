date, name, price = ['Decemeber 23, 2015', 'Bread Gloves', 8.51]
print(date)

def drop_first_last(grades):
    # the '*' only works in python34
    first, *middle, last = grades
    average_of_middle = sum(middle) / len(middle)
    print(average_of_middle)

drop_first_last([54, 99, 67, 55, 43 23])
