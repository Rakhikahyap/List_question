list=[2,2,5,3,7,8,8]
i=0
a=[]
b=[]
c=[]
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
    if list[i]%2==0:
        b.append(list[i])
    else:
        c.append(list[i])
    i+=1
print(a)
print(b)
print(c)