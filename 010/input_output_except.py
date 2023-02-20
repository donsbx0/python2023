try:
    with open('input.inp', 'r', encoding='utf-8') as fileInp:
        ten = fileInp.readline().rstrip('\n')
        tuoiHientai = int(fileInp.readline().rstrip('\n'))

    with open('output.out', 'wb') as fileOut:
        stringToSave = '10 năm nữa, tuổi của {} sẽ là {}'.format(ten, tuoiHientai + 10)
        fileOut.write(stringToSave.encode('utf8'))
except:
    print('File khong hop le')