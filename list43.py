a=[2,[2,3,[4],6]]
i=0
m=[]
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==type([]):
                k=0
                sum=0
                while k<len(a[i][j]):
                    m.append(a[i][j][k])
                    k+=1
                else:
                    m.append(a[i][j])
                j+=1
            else:
                m.append(a[i])
            i+=1