"""
Task:\n Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.

Input Format:
The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks, IDs, name and class, under their respective column names.

Constraints:
0 < N <= 100

Output Format:
Print the average marks of the list corrected to 2 decimal places.
"""



from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    student = namedtuple('student', input())
    print(sum([int(student(*input().split()).MARKS) for _ in range(n)]) / n)