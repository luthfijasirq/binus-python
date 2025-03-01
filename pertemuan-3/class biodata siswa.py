class Siswa:
    def __init__(self, nama, umur, alamat, kelas,):
         self.nama = nama
         self.umur = umur
         self.alamat = alamat
         self.kelas = kelas
         
    def tampilkan_biodata(self):
        print("Biodata Siswa: ")
        print(f"nama: {self.nama}")
        print(f"umur: {self.umur} tahun")
        print(f"alamat: {self.alamat}")
        print(f"kelas {self.kelas}")
        
def input_biodata_siswa():
    nama = input("masukan nama siswa: ")
    umur = input("masukan umur siswa: ")
    alamat = input("masukan alamat siswa: ")
    kelas = input("masukan kelas siswa: ")
        
    siswa = Siswa(nama, umur, alamat, kelas)
    siswa.tampilkan_biodata()
        
input_biodata_siswa()
        
