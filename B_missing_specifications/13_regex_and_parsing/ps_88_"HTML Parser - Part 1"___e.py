"""
You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.
"""


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())