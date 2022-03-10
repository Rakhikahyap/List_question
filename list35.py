list=[[1,2,3],[4,5,6,7],[8,9,10],[11,12]]
i=0
sum=0
m=[]
while i<len(list):
    j=0
    while j<len(list[i]):
        m.append(list[i][j])
        j=j+1
    i=i+1
print(m)