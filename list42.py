a=[[2,3,4],[5,6,2],[1,0,1]]
i=0
m=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    i=i+1
    m.append(sum)
print(m)
