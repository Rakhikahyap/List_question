a=[11,12],[13,14]
i=0
b=[]
while i<len(a):
    k=0
    sum=0
    while k<len(a[i]):
        sum=sum+a[k][i]
        k=k+1
    i=i+1
    b.append(sum)
print(b)