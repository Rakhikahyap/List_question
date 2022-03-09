a=[1,1,1]
sum=0
i=-1
b=0
while i>=-len(a):
    sum=sum+a[i]*2**b
    i=i-1
    b+=1
print(sum)