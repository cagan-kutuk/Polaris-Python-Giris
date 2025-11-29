
name = input("100 yaşınızda yılın kaç olacağını öğrenmeden önce lütfen adınızı ve soyadınızı giriniz.").strip().title()

first = name.split()[0]

print(f"Merhaba, {first}.")

x = int(input("Yaşınızı giriniz."))

if 100 > x  > 0: 
    y = 2025 + (100 - x)
    print(f"100 yaşınızda yıl {y} olacak.")

elif x >= 100:
    print("Zaten 100 yaşını geçmişsiniz.")

else: 
    print("Yaşınızı yanlış girdiniz.") 