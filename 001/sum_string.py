print('Nhao vao cac so co khoang trang: ')
dayGiatri = input()
danhsachGiatri = dayGiatri.split()
Ipokla = False
try:
    danhsachSo = map(int, danhsachGiatri)
    tongDayso = sum(danhsachSo)
    Ipokla = True
except:
    print('Gia tri nhap vao khong hiop le')
if Ipokla:
    print('Tong dang so la: ', tongDayso)