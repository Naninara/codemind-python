r,c=map(int,input().split())
m=[]
e=[]
k=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(c):
    e=[]
    for j in range(r):
        y=(m[j][i])
        e.append(y)
    k.append(e)
c=0
for i in k:
    o=sorted(i)
    y=sorted(i,reverse=True)
    if i==o or i==y:
        c+=1
print(c)