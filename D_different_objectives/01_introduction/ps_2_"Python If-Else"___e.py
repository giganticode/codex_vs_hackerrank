"""
Input an integer n and perform the following conditional actions:

If n is odd, print {Strange}
If n is even and in the inclusive range of 2 to {18}, print Not {Strange}
If n is even and in the inclusive range of {18} to 20, print {Strange}
If n is even and greater than 20, print Not {Strange}

Input Format:
A single line containing a positive integer, n.

Constraints:
1 <= n <= 100

Output Format:
Print {Strange} if the number is {Strange}. Otherwise, print Not {Strange}.
"""

n = int(input())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")