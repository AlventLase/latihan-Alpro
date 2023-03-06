import math

def is_prime(number):
    pembagi = 0
    for i in range(1, int(math.sqrt(number+1))): #pencarian hanya sampai akar n, hanya sampai di atas 1000
        if number % i == 0:
            pembagi += 1
    if pembagi == 2:
        return True
    else:
        return False
    
#batas
number = int(input('Masukkan bilangan: '))
hasil = is_prime(number)
if hasil:
    print('Bilangan prima')
else:
    print('Bukan Prima')