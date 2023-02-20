
suhu = float(input('Masukkan suhu: '))

# if suhu >= 38:
#     print('Demam')
# else:
#     print('Tidak demam')



if suhu <= 34.0:
    print('Mati kedinginan')
elif  34.0 <= suhu <= 37.0:
    print('Aman')
elif 37.1 <= suhu <= 40.0:
    print('Demam')
else:
    print('Mati kedinginan')




# int akan memiliki masalah dalam banyak hal dengan float, maka nilai int diubah menjadi int 34 = 34.0