a=[2,3,8,5,7]
i=0
b=[]
while i<len(a):
    j=1
    c=0
    while j<=a[i]:
        if a[i]%j==0:
            c=c+1
        j=j+1
    if c==2:
        b.append(a[i])
    i=i+1
print(b)