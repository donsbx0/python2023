# Nhap bieu thuc cua ban phim
try:
    print("Nhap hai so va phep tinh vao: ")
    soThu1, phepTinh, soThu2 = input().split()

    #Add du lieu sang so thuc
    soThu1 = float(soThu1)
    soThu2 = float(soThu2)
except:
    print("Loi nhap du lieu")

# Tao bien luu ket qua cua bieu thuc
ketQua = None
# Dung cau lenh re nhanh de phan loai phep tinh

if phepTinh == '+':
    ketQua = soThu1 + soThu2

elif phepTinh == '-':
    ketQua = soThu1 - soThu2

elif phepTinh == '*':
    ketQua = soThu1 * soThu2
elif phepTinh == ':'or '/':
    if soThu2 == 0:
        print("So thu 2 phai khac 0")
    else:
        ketQua = soThu1 / soThu2

# In ket qua ra man hinh
if ketQua != None:
    print("{} {} {} = {}".format(soThu1, phepTinh, soThu2, ketQua))