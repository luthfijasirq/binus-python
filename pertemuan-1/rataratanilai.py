def main():
    nilai_angka = {
        'A': 4.00, 'A-': 3.75, 'B+': 3.50, 'B': 3.00, 'B-': 2.75, 
        'C+': 2.50, 'C': 2.00, 'C-': 1.75, 'D': 1.50, 'E': 1.20
    }
    nilai_huruf = []
    
    while (kategori := input("Masukkan Kategori Nilai (Tekan Enter untuk Berhenti): ")) != "":
        nilai_huruf.append(kategori)
    
    if nilai_huruf:
        rata_rata = sum(nilai_angka[huruf] for huruf in nilai_huruf) / len(nilai_huruf)
        penunjukan = ("A" if rata_rata >= 4.00 else 
                      "A-" if rata_rata >= 3.75 else 
                      "B+" if rata_rata >= 3.50 else 
                      "B" if rata_rata >= 3.00 else 
                      "B-" if rata_rata >= 2.75 else 
                      "C+" if rata_rata >= 2.50 else 
                      "C" if rata_rata >= 2.00 else 
                      "C-" if rata_rata >= 1.75 else
                      "D")
        print(f"Nilai rata-rata adalah {rata_rata:.2f} dengan penunjukan {penunjukan}")

main()
