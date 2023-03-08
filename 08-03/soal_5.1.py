def perkalian(n, m):
    hasil = 0
    print(f"{n} x {m} = ", end="")
    for i in range(1, n+1):
        if i == n:
            print(f"{m} x ", end="")
        else:
            print(f"{m} x ", end="")
        hasil =  hasil + m
    print(f" = {hasil}")

perkalian(6,5)
perkalian(7,10)
perkalian(6,7)