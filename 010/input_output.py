with open('input.inp', 'r') as fileInp:
    ten = fileInp.readline().rstrip('\n')
    tuoiHientai = int(fileInp.readline().rstrip('\n'))

with open('output.out', 'w') as fileOut:
    fileOut.write('20 nam nua, tuoi cua {} se la {}'.format(ten, tuoiHientai+10))