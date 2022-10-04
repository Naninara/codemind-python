n=int(input())
li=list(map(int,input().split()))
s=0
for i in li:
    s=s*10+i
a=str(s)
print(int(a,2))