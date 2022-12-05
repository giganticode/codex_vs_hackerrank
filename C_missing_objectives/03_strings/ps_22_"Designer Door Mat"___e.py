"""
Mr. Vincent works in a door mat manufacturing company. 
"""

def make_mat(rows, cols):
    for i in range(1, rows + 1):
        if i == 1:
            print('WELCOME'.center(cols, '-'))
        elif i == rows:
            print(''.join(['-' for i in range(cols)]))
        else:
            print(''.join(['|' for i in range(cols)]) + '.')


if __name__ == '__main__':
    n, m = map(int, input().split())
    make_mat(n, m)