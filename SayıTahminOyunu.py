
import random

sayi = random.randint(1, 100)

tahmin = None

while tahmin != sayi:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin et: "))
    
    if tahmin < sayi:
        print("Yukarı çık!")
    elif tahmin > sayi:
        print("Aşağı in!")
    else:
        print("Tebrikler, doğru tahmin ettinz!")


#None: boş demektir sadece değer atamadığım değişkeni başlatmak için kullandım.   
