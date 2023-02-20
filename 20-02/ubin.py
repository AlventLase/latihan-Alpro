#input jumlah 1 meter, 5 meter dan panjang
ubin1 = int(input('Masukkan jumlah ubin 1 meter: '))
ubin5 = int(input('Masukkan jumlah ubin 5 meter: '))
panjang = int(input('masukkan panjang yang ditutupi ubin: '))

if (1 * ubin1 + 5 * ubin5) >= panjang:
    #mungkin bisa
    #apakah cukup atau tidak
    if panjang % 5 == 0 and panjang//5 <= ubin5:
        print('Bisa') #jika menggunakan def dari atas, print bisa diganti dengan return True
    elif panjang %5 <= ubin1:
        print('Bisa')
    else:
        print('Tidak bisa') #untuk else -> return False
    

else:
    print('Tidak bisa')