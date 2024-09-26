# bai 16
c = input()
stt = ord(c)
if c == 'z' or c == 'Z':
    print('a')
elif c >= 'A' and c <= 'Z':
    stt += 1
    print(chr(stt).lower())