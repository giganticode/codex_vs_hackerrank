"""
Input in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Input Format:
The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints:
- 2 <= n <= 10
- 0 <= marks[i] <= 100
- length of marks arrays = 3 

Output Format:
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
"""



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{0:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name])))