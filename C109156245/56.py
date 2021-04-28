a = input("請選擇主餐及升級的套餐:")
b=input("是否升級成大杯飲料:")
c=input("是否換成大薯:")
tmp = 0
if a=="1A":
    tmp=72+55
elif a=="1B":
    tmp=72+68
elif a=="2A":
    tmp=62+55
elif a=="2B":
    tmp=62+68
elif a=="3A":
    tmp=82+55
elif a=="3B":
    tmp=82+68 
elif a=="4A":
    tmp=44+55
elif a=="4B":
    tmp=44+68
elif a=="5A":
    tmp=60+55
elif a=="5B":
    tmp=60+68

if b=="是":
    tmp+=7
if c=="是":
    tmp+=13

print(str(tmp))
