import math

# Fungsi untuk menghitung jarak antara dua titik di permukaan bumi
def haversine(lat1, lon1, lat2, lon2):
   
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    R = 6371.0
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    distance = R * c
    return distance

lat1 = float(input("Masukkan latitude titik 1: "))
lon1 = float(input("Masukkan longitude titik 1: "))
lat2 = float(input("Masukkan latitude titik 2: "))
lon2 = float(input("Masukkan longitude titik 2: "))

jarak = haversine(lat1, lon1, lat2, lon2)

print(f"Jarak antara titik 1 dan titik 2 adalah {jarak:.2f} kilometer.")
