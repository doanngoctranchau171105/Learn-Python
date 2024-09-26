# bai 12
def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False
t, n = map(int, input().split())
if (1 <= t <= 12) and n > 0:
    ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (leap_year(n)):
        ngay_trong_thang[1] = 29
    print(ngay_trong_thang[t - 1])
else:
    print('INVALID')
