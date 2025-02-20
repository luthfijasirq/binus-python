def hitung_rata_rata(nilai_huruf):
    # Membuat kamus nilai huruf
    nilai_angka = {
        'A': 4.00,
        'A-': 3.75,
        'B+': 3.50,
        'B': 3.00,
        'B-': 2.75,
        'C+': 2.50,
        'C': 2.00,
        'C-': 1.75,
        'D': 1.50
    }

    total_nilai = 0
    jumlah_data = len(nilai_huruf)

    for huruf in nilai_huruf:
        if huruf in nilai_angka:
            total_nilai += nilai_angka[huruf]
        else:
            print(f"Kategori huruf {huruf} tidak valid!")
            return None
    
    rata_rata = total_nilai / jumlah_data
    return rata_rata

def penunjukan_nilai(rata_rata):

    if rata_rata >= 3.75:
        return "A"
    elif rata_rata >= 3.50:
        return "A-"
    elif rata_rata >= 3.00:
        return "B+"
    elif rata_rata >= 2.75:
        return "B"
    elif rata_rata >= 2.50:
        return "B-"
    elif rata_rata >= 2.00:
        return "C+"
    elif rata_rata >= 1.75:
        return "C"
    elif rata_rata >= 1.50:
        return "C-"
    else:
        return "D"

def main():

    nilai_huruf = []
    
    while True:
        kategori = input("Masukkan Kategori Nilai (Tekan Enter untuk Berhenti): ")
        
        if kategori == "":
            break
    
        nilai_huruf.append(kategori)
    
    rata_rata = hitung_rata_rata(nilai_huruf)
    
    if rata_rata is not None:

        penunjukan = penunjukan_nilai(rata_rata)
        print(f"Nilai rata-rata adalah {rata_rata:.2f} dengan penunjukan {penunjukan}")

main()
