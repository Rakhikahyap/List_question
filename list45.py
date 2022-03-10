chance=int(input("entre no.chance"))
i=0
odd=[]
even=[]
ec=0
oc=0
while i<(chance):
    num=int(input("entre"))
    if num%2==0:
        ec+=1
        even.append(num)
    else:
        oc+=1
        odd.append(num)
    i=i+1
print(even,"even",ec)
print(odd,"odd",oc)