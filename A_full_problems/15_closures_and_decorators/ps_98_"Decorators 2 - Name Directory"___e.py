"""
Let's use decorators to build a name directory! 
You are given some information about N people. Each person has a first name, last name, age and sex. 
Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be:
Mr. Henry Davids

For Mary George, the output should be:
Ms. Mary George

Input Format:
The first line contains the integer N, the number of people.
N lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

Constraints:
1 <= N <= 10

Output Format:
Output N names on separate lines in the format described above in ascending order of age.
"""



def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')