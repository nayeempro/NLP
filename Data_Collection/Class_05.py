n=100
l = []
for i in range(1,n+1):
    if(i>=4 and i<n):
        l.append(4)
    elif(i==n):
        l.append(5)
    else:
        l.append(i)
print(l)
