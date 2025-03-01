class Data:
    def __init__(self):
        self.__nama = None
        self.__skor = None
        
    def get_nama(self):
        return self.__nama
        
    def set_nama(self, nama):
        self.__nama = nama
        
    def get_skor(self):
        return self.__skor
        
    def set_skor(self, skor):
        self.__skor = skor    
    
    def printEmployee(self):
        print("Name:", self.name, "\nSalary:", self.salary)
    
    # Getter Method Declaration
    def tampilkan_data(self):
        if self.__nama is None or self.__skor is None:
            print("Nama: tidak ada")
            print("Skor: tidak ada")
        else:
            print(f"Nama: {self.__nama}")
            print(f"Skor: {self.__skor}")
    
    # Setter Method Declaration
    def hapus_data(self):
        self.__nama = None
        self.__skor = None
        print("data berhasil dihapus")
        
def main():
    data = Data()
    
    while True:
        print("\n===== Program OOP =====")
        print("1. Mendeklarasikan objek")
        print("2. Menampilkan objek")
        print("3. Mengubah nilai objek")
        print("4. Menghapus objek")
        print("5. Keluar dari program")
        
        pilihan = input("Masukan Pilihan anda (1/2/3/4/5):")
        
        if pilihan == "1":
            nama = input("Masukan Nama anda: ")
            skor = input("Masukan skor anda: ")
            
            try:
                skor = int(skor)
                data.set_nama(nama)
                data.set_skor(skor)
                print("data berhasil ditambahkan")
            except ValueError:
                print("skor harus berupa angka")
                
        elif pilihan == '2':
            data.tampilkan_data()
            
        elif pilihan == '3':
            ubah = input("Apa yang ingin anda ubah (Nama/skor): "
                ).lower()
            if ubah == 'nama':
                nama_baru = input("Masukan nama baru: ")
                data.set_nama(nama_baru)
                print("data nama berhasil diubah")
            elif ubah == 'skor':
                skor_baru = input("Masukan skor baru: ")
                try:
                    skor_baru = int(skor_baru)
                    data.set_skor(skor_baru)
                    print("data skor berhasil diubah")
                except ValueError:
                    print("skor harus berupa angka") 
            else:
                print("pilihan tidak valid")
                
        elif pilihan == '4':
            data.hapus_data()
            
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program saya")
            break
         
        else:
            print("Pilihan tidak valid, coba lagi")
              
if __name__ == "__main__":
    main()
