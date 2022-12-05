"""
You are given a set A and n other sets.
"""


def main():
    n = int(input())
    A = set(map(int, input().split()))
    for _ in range(n-1):
        B = set(map(int, input().split()))
        if A.issuperset(B):
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    print("Yes" if main() else "No")