list_1 = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    list_1.append([name,score])

l_score = [x[1] for x in list_1]

min_scr = sorted(set(l_score))

l_name = sorted([y[0] for y in list_1 if y[1] == min_scr[1]])
[print(k) for k in l_name]