n=int(input())
li=list(map(int,input().split()))
li.insert(0,li[n-1])
li.append(li[1])
s=0
for i in range(1,n+2-1):
    if li[i-1]%2==0 and li[i+1]%2!=0 or li[i-1]%2!=0 and li[i+1]%2==0:
        s+=1
print(s)