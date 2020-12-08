# Check if a year is a leap year
def check_leap_year(year):
    # A year is a leap year if it is divisible by 4,
    # and either not divisible by 100, or divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Check if the input year is a leap year
print(check_leap_year(int(input("Enter a year to check: "))))
