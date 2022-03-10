a=[7,9,4,11,90],[440,3,17,2]
i=0
n=[]
while i<len(a[i]):
    j=0
    while j<len(a[i]):
        n.append(a[i][j])
        j=j+1
    i=i+1
print(n)
i=0
while i<len(n):
    j=0
    while j<len(a[i]):
        n.append(a[i][j])
        j=j+1
    i=i+1
print(n)