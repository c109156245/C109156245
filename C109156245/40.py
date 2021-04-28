t = int(input("搭了幾次電梯"))
b=[]
a=1
tmp=0
for i in range(0,t):
    c = input("樓層:")
    b.append(c)
    

    for j in range(len(b)):
        if int(b[i])>a:
            tmp+=(int(b[i])-a)*20
            a=int(b[i])
            
        elif int(b[i])<a:
            tmp+=(a-int(b[i]))*10
            a=int(b[i])

print(str(tmp))