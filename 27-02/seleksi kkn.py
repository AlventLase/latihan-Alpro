def seleksi_kkn(sks):
    #return True: jika bisa ambil kkn, sks >= 110
    #return False: jika sks < 110

    if sks >= 110:
        return True
    else:
        return False

#Program utama
#input sks yang sudah diambil
sks = int(input('Masukkan junlah sks yang sudah ditempuh: '))
#Proses
hasil_seleksi = seleksi_kkn(sks)

#output
if hasil_seleksi == True:
    print('Boleh mengambil KKN')
else:
    print('Tidak boleh mengambil KKN')


# satu fungsi hanya untuk satu kegunaan