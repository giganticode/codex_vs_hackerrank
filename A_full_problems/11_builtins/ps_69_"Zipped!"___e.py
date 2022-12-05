"""
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

The format for the general mark sheet is:
Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5 

Average score = Sum of scores obtained in all subjects by a student / Total number of subjects

Input Format:
The first line contains N and X separated by a space.
The next X lines contains the space separated marks obtained by students in a particular subject.

Constraints:
0 < N <= 100
0 < X <= 100

Output Format:
Print the averages of all students on separate lines.
The averages must be correct up to 1 decimal place.
"""



n, x = map(int, input().split())

scores = []
for _ in range(x):
    scores.append(map(float, input().split()))

for i in zip(*scores):
    print(sum(i) / x)