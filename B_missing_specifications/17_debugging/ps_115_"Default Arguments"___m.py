"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Python supports a useful concept of default argument values. For each keyword argument of a function, we can assign a default value which is going to be used as the value of said argument if the function is called without it. 

For example, consider the following increment function:
def increment_by(n, increment=1):
    return n + increment
    
The functions works like this:
>>> increment_by(5, 2)
7
>>> increment_by(4)
5
>>>

Debug the given function print_from_stream using the default value of one of its arguments.
The function has the following signature:
def print_from_stream(n, stream)

This function should print the first n values returned by get_next() method of stream object provided as an argument. Each of these values should be printed in a separate line.

Whenever the function is called without the stream argument, it should use an instance of EvenStream class defined in the code stubs below as the value of stream.
Your function will be tested on several cases by the locked template code.
"""



class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())