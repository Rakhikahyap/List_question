a=[1,2,3,4,5]
i=0
c=0
sum=0
while i<len(a):
    sum=sum+a[i]
    c+=1
    i+=1
    print(sum//c)