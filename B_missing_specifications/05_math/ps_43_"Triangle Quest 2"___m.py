"""
Input a positive integer N.
Your task is to print a palindromic triangle of size N.
You have to complete the code using exactly one print statement within a for loop.
"""



for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i-1)//9)**2)