m = int(input("請輸入階層值M:"))
a = 1
n = 1
while n<m:
    n = n*a
    a+=1
print("超過M為"+str(m)+"的最小階層值為:"+str(a-1))
