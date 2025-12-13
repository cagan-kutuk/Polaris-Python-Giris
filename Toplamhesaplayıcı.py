
T = 0

while True:
    
    
    N = int(input("Lütfen pozitif bir sayı giriniz: "))

    if N > 0:
        break
    else:
        print("Yanlış sayı girdiniz.")

for i in range(1, N + 1):
    T += i

print(T)
