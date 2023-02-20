cigars = int(input('Masukkan jumlah'))
weekend = input('Apakah weekend? (Y/N): ')
is_weekend = False #agar sintag bawah tidak error

if weekend == 'Y' or weekend == 'y':
    is_weekend = True

if (is_weekend == True and cigars >= 40):
    print('Sukses')
elif is_weekend == 