try:
    a = int(input())
    b = int(input())

    if a > b:
        print("So thu nhat lon hon so thu hai")
    else:
        dem = 0
        for i in range(a,b+1):
            if i % 5 ==0:
                print(i)
                dem+=1
                if dem > 10:
                    break

except:
    print("Dau Vao khong hop le")