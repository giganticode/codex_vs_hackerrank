"""
You are given a list of N lowercase English letters. 
For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.
"""


from itertools import combinations

def find_prob(input_list, num):
    total_combinations = list(combinations(input_list, num))
    count = 0
    for i in total_combinations:
        if 'a' in i:
            count += 1
    return count/len(total_combinations)

if __name__ == "__main__":
    input_list = ['a', 'b', 'c', 'd', 'e', 'f']
    num = 3
    print(find_prob(input_list, num))