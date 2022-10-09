n=int(input())
li=list(map(int,input().split()))
a=[]
for i in li:
	if i not in a:
		print(i,end=' ')
		a.append(i)