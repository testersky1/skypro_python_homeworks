def year_is_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

test_year_1 = 2024
test_year_2 = 2007
is_leap_1 = year_is_leap(test_year_1)
is_leap_2 = year_is_leap(test_year_2)

print(f"Год {test_year_1} високосный: {is_leap_1}")
print(f"Год {test_year_2} високосный: {is_leap_2}")