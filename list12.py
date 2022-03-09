a=[1,0,1,1,1]
n=0
i=0
sum=0
while i<len(a):
    sum=(a[i]*2**i+sum)
    i=i+1
print(sum)