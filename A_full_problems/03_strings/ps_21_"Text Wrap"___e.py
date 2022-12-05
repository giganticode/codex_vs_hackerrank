"""
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Function Description:
Make a wrap function.
wrap has the following parameters:
string string: a long string
int max_width: the width to wrap to

Returns:
string: a single string with newline characters ('\n') where the breaks should be.

Input Format:
The first line contains a string, S.
The second line contains the width, w.

Constraints:
0 < len(S) < 100
0 < w < len(S)
"""



def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)