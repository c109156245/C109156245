a = input("請輸入一組四位數字為:")
b=[]
for i in range(len(a)):
    c=(int(a[i])+7)%10
    str(c)
    b.append(c)
    


print("輸出加密後的數字為:%d%d%d%d" %(b[2],b[3],b[0],b[1]))


