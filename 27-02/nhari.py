

def n_hari_berikutnya(nama, n):
    n = n % 7
    if nama == 'senin':
        if n == 0:
            print('senin')
        elif n == 1:
            print('selasa')
        elif n == 2:
            print('rabu')
        elif n == 3:
            print('kamis')
        elif n == 4:
            print('jumat')
        else:
            print('sabtu')

def n_hari_berikutnya(nama, n):
    n = n % 7
    #wajib menggunakan list
    '''
    senin = 0  
    selasa = 1
    rabu = 2
    kamis = 3
    jumat = 4
    sabtu = 5
    minggu = 6
    '''

    
    bobot = 0
    if nama == 'selasa':
        bobot = 1
    elif nama == 'rabu':
        bobot = 2
    elif nama == 'kamis':
        bobot = 3
    elif nama == 'jumat':
        bobot = 4
    elif nama == 'sabtu':
        bobot = 5
    elif nama == 'minggu':
        bobot = 6
    
    total = (bobot + n) % 7
    if bobot == 0:
        print('senin') #untuk submit wajib menggunakan huruf kecil
    elif bobot == 1:
        print('selasa')
    elif bobot == 2:
        print('rabu')
    elif bobot == 3:
        print('kamis')
    elif bobot == 4:
        print('jumat')
    elif bobot == 5:
        print('sabtu')
    elif bobot == 6:
        print('minggu')


nama = input('Masukkan nama: ')
n = int(input('Berapa hari kemudian?: '))
n_hari_berikutnya(nama, n)