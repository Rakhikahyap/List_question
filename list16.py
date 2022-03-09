a=[50,40,23,70,56,12,5,10,7]
max1=0
max2=0
max3=0
i=0
while i<len(a):
    if a[i]>max1:
        max1=a[i]
    elif a[i]>max2:
        max2=a[i]
    elif a[i]>max3:
        max3=a[i]
    i+=1
print(max1)
print(max2)
print(max3)