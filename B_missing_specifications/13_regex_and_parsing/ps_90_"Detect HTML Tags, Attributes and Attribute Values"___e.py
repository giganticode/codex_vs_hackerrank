"""
You are given an HTML code snippet of N lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.
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