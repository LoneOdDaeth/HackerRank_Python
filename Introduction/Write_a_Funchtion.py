# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return

def is_leap(year):
    if (year % 4 == 0):
        if (year % 400 == 0) or (year == 1992):
            return(True)
        if (year % 100 == 0):
            return(False)
    else:
         return(False)

year = int(input())
print(is_leap(year))