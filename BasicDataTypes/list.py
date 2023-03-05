N = int(input())

list_1 = []

for i in range(N):
    index = list(input().split())
    if index[0] == "insert":
        list_1.insert(int(index[1]),int(index[2]))
    if index[0] == "print":
        print(list_1)
    if index[0] == "remove":
        list_1.remove(int(index[1]))
    if index[0] == "append":
        list_1.append(int(index[1]))
    if index[0] == "sort":
        list_1.sort()
    if index[0] == "pop":
        list_1.pop()
    if index[0] == "reverse":
        list_1.reverse()