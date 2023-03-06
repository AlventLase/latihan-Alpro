def is_prime(number):
    pembagi = 0
    for i in range(1, number+1): #stopnya selalu ditambah 1
        if number % i == 0:
            pembagi += 1 #sama dengan pembagi =  pembagi + 1
    if pembagi == 2:
        return True
    else:
        return False
    
#program utama
number = int(input('Masukkan bilangan: '))
hasil = is_prime(number)
if hasil:
    print('Bilangan prima')
else:
    print('Bukan Prima')