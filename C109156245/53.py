a=float(input("請輸入路程公里數(km):"))
if a<=1.5:
    print("所需車資為:75")
else:
    b=a-1.5
    c=b//0.25
    q=b%0.25
    sum1 = 75+c*5
    if q!=0:
        sum1 +=5
    
    print(str("%d" %sum1))


