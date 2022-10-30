r,c=map(int,input().split())
m=[]
e=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(r):
    e.append(sum(m[i]))
for i in range(c):
    s=0
    for j in range(r):
        s+=m[j][i]
    e.append(s)
print(max(e))