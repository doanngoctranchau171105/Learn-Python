# bai 14
a, b, c, d = map(float, input().split())
tb = (a + b + c * 2 + d * 3) / 7
if tb >= 8:
    print('GIOI')
elif tb >= 6.5:
    print('KHA')
elif tb >= 5:
    print('TRUNG BINH')
else:
    print('YEU')