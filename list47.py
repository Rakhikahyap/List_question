n=[1,2,4,6,5,8,7,9,10,11]
i=0
while i<len(n):
    if n[i]%2==0:
        print("even",n[i])
    else:
        print("odd",n[i])
    i=i+1