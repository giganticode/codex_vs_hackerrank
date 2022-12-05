"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring:
A player gets +1 point for each occurrence of the substring in the string S.
"""


def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += (len(string) - i)
        else:
            stuart_score += (len(string) - i)
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)