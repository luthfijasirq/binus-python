while True:

    
    def jenis_segitiga(a, b, c):
    
        if a + b <= c or a + c <= b or b + c <= a:
            return "Bukan Segitiga"
    
        elif a == b == c:
            return "Segitiga Sama Sisi"
    
        elif a == b or b == c or a == c:
            return "Segitiga Sama Kaki"
    
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Segitiga Siku-Siku"
    
        else:
            return "Segitiga Sisi Tak Sama Panjang"

    a = float(input("Masukkan Sisi A: "))
    b = float(input("Masukkan Sisi B: "))
    c = float(input("Masukkan Sisi C: "))

    hasil = jenis_segitiga(a, b, c)

    print("Ini adalah ", hasil)
    
    ulang = input("Apakah Anda ingin mengulang? (Y/N): ").upper()
    
    if ulang == 'N':
        print("Program Berhenti Terima kasih telah menggunakan program saya")
        break
    elif ulang != 'Y':
        print("Input tidak valid, program berhenti.")
        break
