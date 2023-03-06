import random

def generate_angka(bawah, atas):
    angka_komputer = random.randrange(bawah, atas)
    return angka_komputer

#program utama
#print(generate_angka)

angka_komputer = generate_angka(0, 100)
tebakan = False
while tebakan == False:
    tebakan_user = int(input('Masukkan tebakan anda: '))
    if tebakan_user == angka_komputer:
        tebakan = True
    else:
        if tebakan_user> angka_komputer:
            print('Tebakan anda terlalu besar')
        else:
            print('Tebakan anda terlalu kecil')
        print('Tebakan anda masih salah! silahkan coba lagi')

print('Selamat, tebakan anda benar') # cara agar bisa menemukan, cari nilai tengah, 100/2 = 50, 50/2 = 25
#binary search, 