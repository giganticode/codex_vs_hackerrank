"""
You are given n words. Some words may repeat. 
For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.
"""


from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    word = input()
    d[word] = d.get(word, 0) + 1
print(len(d))
print(*d.values())