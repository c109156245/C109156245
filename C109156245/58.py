a=[]
for i in range(1,11):
    x = input("請輸入第%d個數字:" %i)
    a.append(x)

a.sort()

print(("最大的3個數字為:"+a[9]+","+a[8]+","+a[7]))
print(("最小的3個數字為:"+a[2]+","+a[1]+","+a[0]))