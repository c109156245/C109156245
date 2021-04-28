
a =input("輸入五張牌:")
b=a.split()




tmp=0
for i in range(len(b)):
    if b[i] == "A":
        tmp+=1
    elif b[i]=="J":
        tmp+=11
    elif b[i]=="Q":
        tmp+=12
    elif b[i]=="K":
        tmp+=13
    else:
        tmp+=int(b[i])
print(str(tmp))


