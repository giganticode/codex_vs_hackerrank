"""
Input an integer n and perform the following conditional actions:
"""

n = int(input("Enter a number: "))

if n % 2 == 0:
    if n % 3 == 0:
        print("Divisible by 3 and 2")
    else:
        print("Divisible by 2 not divisible by 3")
else:
    if n % 3 == 0:
        print("Divisible by 3 not divisible by 2")
    else:
        print("Not divisible by 2 not divisible by 3")