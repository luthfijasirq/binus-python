def tulis_biodata():
    
    nama = input("Nama: ")
    umur = input("umur: ")
    alamat = input("Alamat : ")
    email = input("email : ")

    with open("Biodata.txt", "w") as file:
       file.write(f"Nama: {nama}\n")
       file.write(f"Umur: {umur}\n")
       file.write(f"Alamat: {alamat}\n")
       file.write(f"Email: {email}\n")
    print("Biodata berhasil disimpan")

def baca_biodata(): 
    try:
        with open("Biodata.txt", "r") as file:
            print("\nIsi biodata: ")
            print(file.read())
    except FileNotFoundError:        
        print("Biodata berhasil disimpan")  


tulis_biodata()
baca_biodata()        
          
