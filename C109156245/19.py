a = int(input("組數為:"))
b=[]
for i in range(0,a):
    c=input("第"+str(i+1)+"組:").split(" ")
    b.append(int(c[0])*250 + int(c[1])*175)
    print(b)
for j in range(0,a):
    print("第"+str(j+1)+"組應收費用:"+str(b[j]))




