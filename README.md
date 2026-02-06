# Python-Practice
Python functions to calculate leap years, days in a month, and the day number within a year.
# Date Utilities in Python

This project contains simple Python functions for working with dates using
Gregorian calendar rules.

## Features

- Check whether a year is a leap year
- Get the number of days in a given month
- Calculate the day number within a year (e.g., Dec 31 → day 366 in a leap year)

## Functions

### `is_year_leap(year)`
Returns `True` if the given year is a leap year, otherwise `False`.

### `days_in_month(year, month)`
Returns the number of days in the specified month and year.
Returns `None` for invalid input.

### `day_of_year(year, month, day)`
Returns the day number within the year (1–365 or 1–366).
Returns `None` if the date is invalid.

## Example

```python
print(day_of_year(2000, 12, 31))

## codes
```python
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2000, 12, 31))
