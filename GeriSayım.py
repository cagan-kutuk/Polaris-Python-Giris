
import time


while True:
    sayi = int(input("Geri sayımın başlayacağı saniyeyi belirleyiniz: "))
    
    if sayi > 0:
        break
    else:
        print("Lütfen doğru bir sayı giriniz.")

for i in range(sayi, 0, -1):
    print(i, end="... ", flush=True)
    time.sleep(1)

print("Ateşle!")



#time.sleep(1) sayesinde her sayıyı 1 saniye fark ile yazar ancak onları ekrana yazmıyor
#tüm işlemler bittikten sonra yazıyor tek tek yazması için flush kullanmamız gerek, 
#gerçek tanımı ile tamponu zorla boşalt anlamına geliyor. Tampon ekrana yazmadan önce
#verileri biriktirdiği yerdir. 