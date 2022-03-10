num=list(input("enter"))
i=0
a=""
while i<len(num):
    b=int(num[i])**2
    a=a+str(b)
    i=i+1
print(a)