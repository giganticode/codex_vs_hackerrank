"""
Task:\n Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.
"""


from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    student = namedtuple('student', input())
    print(sum([int(student(*input().split()).MARKS) for _ in range(n)]) / n)