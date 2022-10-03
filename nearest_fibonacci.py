n = int(input())
a=0
b=1
while b<=n:
    a,b=b,a+b
if n-a<b-n:
    print(a)
elif b-n<n-a:
    print(b)
else:
    print(a,b)