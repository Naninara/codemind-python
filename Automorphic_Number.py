n = int(input())
s = str(n)
k = n*n
r = str(k)
if r.endswith(s)==True:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')