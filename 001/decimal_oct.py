giatriA = input()
giatriB = input()

InputOkla = False
try: 
    SoA = float(giatriA)
    SoB = int(giatriB)
    InputOkla = True
except:
    print("Dinh dang dau vao khong hop le")

if InputOkla: 
    print('Dung format: {0:.{1}f}'.format(SoA, SoB))
    formatNum = round(SoA, SoB)
    print('Dung round', formatNum)