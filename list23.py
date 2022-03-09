a=[12,67,43,32,76,12,32,12]
i=0
min=a[0]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i=i+1
print(min)