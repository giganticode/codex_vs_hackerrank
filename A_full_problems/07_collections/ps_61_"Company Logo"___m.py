"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
They are now trying out various combinations of company names and logos based on this condition. 
Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Input Format:
A single line of input containing the string S.

Constraints:
3 < len(S) <= 10^4
S has at least 3 distinct characters

Output Format:
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
"""




from collections import Counter

if __name__ == '__main__':
    s = input()
    c = Counter(s)
    for i in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(*i)