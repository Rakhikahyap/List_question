a=[1,2,-3,-4,5,-6]
i=0
m=[]
while i<len(a):
    if a[i]>0:
        k=a[i]
        m.append(k)
    else:
        n=('0')
        m.append(n)
    i+=1
print(m)