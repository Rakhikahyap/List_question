number=30
n=[10,11,12,13,14,17,18,19]
i=0
a=[]
while i<len(n):
    j=i
    a2=[]
    while j<len(n):
        m=n[i]+n[j]
        if m==30:
            a2.append(n[i])
            a2.append(n[j])
            a.append(a2)
        j+=1
    i+=1
print(a)