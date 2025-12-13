
while True:
    
    try:
    
        sayi = int(input("Lütfen bir sayı giriniz: "))
       
        break  
    
    except ValueError:
        print("Hata: Lütfen geçerli bir tam sayı giriniz.")

print(f"Tebrikler! {sayi} sayısını girdiniz.")
