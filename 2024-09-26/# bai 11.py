# bai 11
def tam_giac(a, b, c):
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        return True
    return False
a, b, c = map(int, input().split())
if not tam_giac(a, b, c):
    print('INVALID')
elif a == b == c:
    print(1)
elif a == b or b == c or a == c:
    print(2)
elif (a * a == b * b + c * c) or (a * a == b * b + c * c) or (a * a == b * b + c * c):
    print(3)
else:
    print(4)

