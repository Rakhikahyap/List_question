
a=["my name is rakhi","i have apple"]
i=0
n=[]
while i<len(a):
    b=a[i].split()
    i=i+1
    n.append(b)
c=0
j=0
while j<len(n):
    l=0
    while l<len(n[j]):
       c=c+1
       l=l+1
    j=j+1
print("count:",c)