a=["r","a","k","h","i"]
i=0
n=[]
str=''
while i<len(a):
    if'' not in  a[i]:
        str+=a[i]
    else:
        n.append(a[i])
    i=i+1
print(str)