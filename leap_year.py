def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            print("True")
        else:
            print("False")
    else:
        if year % 4 == 0:
            print("True")
        else:
            print("False")
is_leap_year(2019)