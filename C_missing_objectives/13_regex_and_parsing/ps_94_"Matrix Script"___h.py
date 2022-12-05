"""
Neo has a complex matrix script. The matrix script is a N x M grid of strings. 
"""

def decode(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = ''
    for i in range(m):
        for j in range(n):
            result += matrix[j][i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(n):
        s.append(input())

    result = decode(s)

    fptr.write(result + '\n')

    fptr.close()