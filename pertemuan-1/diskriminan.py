# Program untuk menghitung diskriminan 

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

D = b**2 - 4*a*c

print(f"Diskriminan (D) = {D}")

if D > 0:
    print("Persamaan memiliki dua akar real dan berbeda.")
elif D == 0:
    print("Persamaan memiliki satu akar real (akar kembar).")
else:
    print("Persamaan memiliki dua akar kompleks (akar imajiner).")