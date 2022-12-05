"""
You are given a valid XML document, and you have to print its score. 
The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has.

Input Format:
The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

Output Format:
Output a single line, the integer score of the given XML document.
"""



import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return len(node.attrib) + sum(get_attr_number(child) for child in node)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
    