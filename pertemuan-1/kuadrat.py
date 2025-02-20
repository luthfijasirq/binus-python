import math

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

if a == 0:
    print("Ini bukan persamaan kuadrat karena a = 0.")
else:

    diskriminan = b**2 - 4*a*c
    
    if diskriminan > 0:
        akar1 = (-b + math.sqrt(diskriminan)) / (2 * a)
        akar2 = (-b - math.sqrt(diskriminan)) / (2 * a)
        print(f"Persamaan kuadrat memiliki dua akar yang berbeda: {akar1} dan {akar2}")
    elif diskriminan < 0:
        print("Persamaan kuadrat memiliki akar imajiner.")
    else:
        akar = -b / (2 * a)
        print(f"Persamaan kuadrat memiliki akar ganda: {akar}")
