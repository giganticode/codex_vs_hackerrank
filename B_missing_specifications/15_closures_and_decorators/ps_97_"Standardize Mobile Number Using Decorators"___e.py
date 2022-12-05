"""
You are given N mobile numbers. 
Sort them in ascending order then print them in the standard format shown below:
+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. 
Alternatively, there may not be any prefix at all.
"""

n = int(input())

numbers = []

for i in range(n):
    numbers.append(input())

numbers.sort()

for i in numbers:
    print("+91 {} {}".format(i[-10:-5], i[-5:]))