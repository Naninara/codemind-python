n = int(input())
f=0
li = list(map(int,input().split()))
for ele in li:
    if ele%2==0:
        f=f+1
if f==len(li):
    print(True)
else:
    print(False)