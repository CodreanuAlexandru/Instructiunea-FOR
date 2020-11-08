n=eval(input("Introduceti n="))
s=0
for a in range(1,n+1):
    if (a%3==0 and a%5==0):
        s+=a
print(s)