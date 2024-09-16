from itertools import permutations
text, per = map(str,input().split(" "))
ls = []
for i in text:
    ls.append(i)
ls.sort()

for c in list(permutations(ls,int(per))):
    print("".join(c))