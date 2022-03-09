numbers=[50,40,23,70,56,12,5,10,7]
i=0
max=0
smax=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
smax=0
i=0
while i<len(numbers):
    if numbers[i]<max and numbers[i]>smax:
        smax=numbers[i]

    i=i+1
print(smax)