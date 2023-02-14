angka =input('masukkan angka (0-9999): ')

# ribuan = angka//1000
# angka = angka%1000
# ratusan = angka//100
# angka = angka%100
# puluhan = angka//10
# angka = angka%10
# satuan = angka//1
# angka = angka%1
# total = ribuan + ratusan + puluhan + satuan

total = 0

for digit in angka:
    total = total + int(digit)

# print(ribuan)
print('Total semua digit: ', total)


