"""
Given a year, determine whether it is a leap year. 

If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format:
Read year, the year to test.

Constraints:
1900 <= year <= 10^5

Output Format:
The function must return a Boolean value (True/False).
"""



def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))