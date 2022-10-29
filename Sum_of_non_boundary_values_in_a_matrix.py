r,c=map(int,input().split())
mat=[]
s=0
for i in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
for i in range(1,r-1):
    for j in range(1,c-1):
        s+=mat[i][j]
print(s)