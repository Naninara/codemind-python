
def cnt(n):
    s=0
    while n>0:
        r = n%10
        s = s+1
        n = n//10
    return (s)
n = int(input())
li = list(map(int,input().split()))
li1=list(map(cnt,li))
k = min(li1)
f=0
for ele in li1:
    if ele==k:
        f=f+1
print(f)