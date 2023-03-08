batas_atas = int(input("Masukkan batas atas: "))
batas_bawah = int(input("Masukkan batas bawah: "))

if batas_bawah > batas_atas: #dibalik
    # batas_atas, batas_bawah = batas_bawah, batas_atas  #tuple
    for i in range(batas_bawah, batas_atas-1, -1):    #ada alasannya, jadi cari sendiri
        if i%2 == 1:
            if i == batas_atas or i == batas_atas +1:
                print(i)
            else:
                print(i, end=", ")
else:
    for i in range(batas_bawah , batas_atas +1):    #ada alasannya, jadi cari sendiri
        if i%2 == 1:
            if i == batas_atas or i == batas_atas -1:
                print(i)
            else:
                print(i, end=", ")
