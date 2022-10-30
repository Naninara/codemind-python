r,c=map(int,input().split())
m=[]
e=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
s=0
for i in m:
    j=i.copy()
    k=i.copy()
    i.sort()
    k.sort(reverse=True)
    if i==j or j==k:
        s+=1
print(s)