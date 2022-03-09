a=[1,2,3,4,5,6]
b=[7,8,9,10,11,12]
i=0
sum=0
m=[]
while i<len(a):
    while i<len(b):
        c=a[i]+b[i]
        i=i+1
        m.append(c)
print(m)