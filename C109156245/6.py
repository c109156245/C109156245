a = list(input("number:"))
for j in range(len(a) - 1):
    for i in range(len(a) -j-1):
        if a[i] > a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
           
        m = a
str1 = "".join(m)

for j in range(len(a) - 1):
    for i in range(len(a) -j-1):
        if a[i] < a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
        mi = a
str2 = "".join(mi)

print(int(str2)-int(str1))
