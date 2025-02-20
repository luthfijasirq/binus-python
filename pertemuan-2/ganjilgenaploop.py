while True:

    int_angka = int(input("Masukan Angka Bebas:"))

    if((int_angka%2)==0):
        print(f"Angka {int_angka} Genap")
    else:
        print(f"Angka {int_angka} ganjil")
        
    ulang = input("Apakah Anda ingin mengulang? (Y/N): ").upper()
    
    if ulang == 'N':
        print("Program Berhenti Terima kasih telah menggunakan program saya")
        break
    elif ulang != 'Y':
        print("Input tidak valid, program berhenti.")
        break
