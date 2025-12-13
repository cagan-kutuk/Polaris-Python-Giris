

Liste = [1,2,3,4,5,6,7,8,9]
Liste2 = [1,2,3,4,5,6,7,8,9]

for a in Liste:
    for b in Liste2:
        print(f"{a}x{b}={a*b}".rjust(6), end=" ")

    print()

#print() her satır sonunda alt satıra geçsin diye.
#end=" " yan yana yazması için
#rjust(6) ise sütunları 6 birimlik sağa yaslaması için