indo = int(input('Rp. '))
usd = indo/14900
yen = indo/130
eur = indo/16700
aud = indo/11500

print(' nilai usd = %.2f' %(usd))
print(' nilai yen = %.2f' %(yen))
print(' nilai eur = %.2f' %(eur))
print(' nilai aud = %.2f' %(aud))

print('Rupiah\t\tUSD\t\tYen\t\tEur\t\tAUD')
print('%d\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f' % (indo, usd, yen, eur, aud))
