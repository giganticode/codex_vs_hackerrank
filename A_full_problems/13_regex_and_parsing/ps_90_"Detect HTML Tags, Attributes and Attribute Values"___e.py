"""
You are given an HTML code snippet of N lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.

Input Format:
The first line contains an integer N, the number of lines in the HTML code snippet.
The next N lines contain HTML code.

Constraints:
0 < N < 100

Output Format:
Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.
Format your answers as explained in the problem statement.
"""



from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()