def solve(s):
    splt = s.split(" ")
    splt1=[]
    for i in splt:
        splt1.append(i.capitalize())
    return " ".join(splt1)

if __name__ == '__main__':

    s = input()
    
    result = solve(s)
    
    print(result + '\n')