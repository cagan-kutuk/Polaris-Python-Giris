
from datetime import datetime

while True:
    try:
        tarih = input("Sınav tarihini giriniz. ")
        saat = input("Sınav saatini giriniz. ")

        sinavzamani = datetime.strptime(tarih + " " + saat,"%d/%m/%Y %H:%M") #tarih ve saati bir araya getirme
        break   

    except ValueError:
        print("Lütfen tarihi doğru bir şekilde girin.")


simdi = datetime.now()

fark = sinavzamani - simdi

if fark.total_seconds() <= 0:             #total_second zaman farkını saniye cinsinden verir 
    print("Bu sınavın zamanı geçmiş.")
else:
    gun = fark.days
    saat = fark.seconds // 3600
    dakika = (fark.seconds % 3600) // 60   #kalan saniyeleri saat ve dakikaya çevirdim


    print(f"Sınava {gun} gün {saat} saat {dakika} dakika kaldı.")


