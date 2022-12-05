"""
The defaultdict tool is a container in the collections class of Python. 
"""

from collections import defaultdict

# Create a list of items
word_list = ['apple', 'banana', 'grapes', 'pear']

# Create a dictionary of counts
count_dict = defaultdict(int)

# Iterate through the list of items, and count each item.
for item in word_list:
    count_dict[item] += 1

# Print the result
print(count_dict)