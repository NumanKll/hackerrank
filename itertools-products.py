A = input().split(" ")

B = input().split(" ")

AxB = []
for i in A:
    for j in B:
        AxB.append((int(i),int(j)))

print(*AxB)