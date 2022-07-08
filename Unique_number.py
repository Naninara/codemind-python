n = int(input())
k = str(n)
li = []
while n>0:
    r=n%10
    li.append(r)
    n = n//10
l = set(li)
if len(k)==len(l):
    print('Unique Number')
else:
    print('Not Unique Number')
    
