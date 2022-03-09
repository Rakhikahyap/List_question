a=[2,3,5,8]
i=0
b=[]
c=[]
while  i<len(a):
    if a[i] not in a:
        a.append(a[i])
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
    i=i+1
print(b)
print(c)