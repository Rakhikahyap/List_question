list=[6,1,3,5,6,3,1]
i=0
a=[]
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
    i=i+1
j=0
n=1
while j<len(a):
    n=n*a[j]
    j=j+1
print(n)