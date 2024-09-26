# bai 15
n, a, b = map(int, input().split())
if a > b/2:
    if n % 2 == 0:
        print((n / 2) * b)
    else:
        loai_2 = n // 2 * b
        loai_1 = n % 2 * a
        print(loai_1 + loai_2)
else:
    print(n * a)
