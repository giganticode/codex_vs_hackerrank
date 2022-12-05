"""
Read a given string, change the character at a given index and then print the modified string.

Function description:
Make a function mutate_string.
mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert

Input Format:
The first line contains a string, string.
The next line contains an integer position, the index location and a string character, separated by a space.
"""



def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)