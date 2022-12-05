"""
Mr. Anant Asankhya is the manager at the INFINITE hotel. 
"""




k = int(input())
room_list = list(map(int, input().split()))

room_set = set(room_list)
print(((sum(room_set)*k) - (sum(room_list)))//(k-1))