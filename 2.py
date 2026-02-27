harga = float(input("Harga :"))

if harga >=100000 :
    diskon = 0.1 * harga
else :
    diskon = 0

total = harga - diskon

print("total bayar :", total )




