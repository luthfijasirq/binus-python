def buat_file(nama_file):
    
    try:
        with open(nama_file, 'r') as file:
            print(f"\nIsi file {nama_file}:")
            print(file.read())
    except FileNotFoundError:
        print(f"\nFile {nama_file} tidak ditemukan. File baru akan dibuat.")

def tampilkan_menu():
   
    print("\nMenu:")
    print("1. Membaca file")
    print("2. Menambahkan teks ke file")
    print("3. Tutup")
    pilihan = input("Pilih opsi (1/2/3): ")
    return pilihan


def tambah_teks(nama_file):
    
    teks = input("Masukkan teks yang akan ditambahkan: ")
    with open(nama_file, 'a') as file:  # Mode 'a' untuk menambahkan teks
        file.write(teks + '\n')
    print(f"Teks telah ditambahkan ke dalam {nama_file}")

def main():
   
    nama_file = input("Masukkan nama file (misalnya: file.txt): ")
    
    while True:
        pilihan = tampilkan_menu()
        
        if pilihan == '1':
            buat_file(nama_file)
        elif pilihan == '2':
            
            tambah_teks(nama_file)
        elif pilihan == '3':
            
            print("Program ditutup.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


main()
