def happy_num(n):
    s = 0
    while n > 0:
        r = n % 10
        s = s + r ** 2
        n = n // 10
    return s
x = int(input())
happy_num(n=x)
happy=1
if x > 9:
    while x > 9:
        x = happy_num(x)
    if x ==happy:
        print('True')
    else:
        print('False')
else:
    print('False')

