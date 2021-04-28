n = int(input("請輸入n:"))
k = int(input(("請輸入k:")))


sum1 = n

while n>=k:
    a = n//k
    sum1 +=a
    n = a


print(str(sum1))