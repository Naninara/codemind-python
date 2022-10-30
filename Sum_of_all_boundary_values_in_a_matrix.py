r,c=map(int,input().split())
mat=[]
for i in range(r):
    li=list(map(int,input().split()))
    mat.append(li)
s=0
for i in range(1,r-1):
    for j in range(1,c-1):
        s=s+mat[i][j]
f=0
for i in range(r):
    for j in range(c):
        f=f+mat[i][j]
print(abs(s-f))