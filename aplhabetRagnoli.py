def print_rangoli(size):
    import string
    rz = list(string.ascii_lowercase)[:size]
    sz = rz[::-1]
    pr = []
    rp = []
    
    for i in range(len(sz)):
        for r in range(0,i+1):
            rp.append(sz[r])
        for j in range(i-1,-1,-1):
            rp.append(sz[j])
        pr.append("".join(rp))
        rp=[]
    loop=0
    for p in range(0,len(pr)):
        print("-"*(((len(pr)*2)-2)-(loop)),end="")
        print("-".join(pr[p]),end="")
        print("-"*(((len(pr)*2)-2)-(loop)))
        loop+=2
    loop=0
    for c in range(len(pr)-2,-1,-1):
        print("-"*(loop+2),end="")
        print("-".join(pr[c]),end="")
        print("-"*(loop+2))
        loop+=2

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)