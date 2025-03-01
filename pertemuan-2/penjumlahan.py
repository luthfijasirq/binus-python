def fg_int_tambah(l_int_angka1 = 1, l_int_angka2 = 1):
    l_int_hasil = l_int_angka1 + l_int_angka2
    return l_int_hasil
    
def fg_int_kurang(l_int_angka1 = 1, l_int_angka2 = 1):
    l_int_hasil = l_int_angka1 - l_int_angka2
    return l_int_hasil
    
def fg_int_kali(l_int_angka1 = 1, l_int_angka2 = 1):
    l_int_hasil = l_int_angka1 * l_int_angka2
    return l_int_hasil
    
def fg_int_bagi(l_int_angka1 = 1, l_int_angka2 = 1):
    if l_int_angka2 == 0:
        return "Error: Pembagian dengan nol"
    l_int_hasil = l_int_angka1 / l_int_angka2
    return l_int_hasil    


def cetak_nama_asal():
    print("------------------------------")
    print("| lutfi jasir quthb |")
    print("|------------------ |")
    print("-" * 30)  


while True:
    cetak_nama_asal()  
    
    
    menu = input("Enter menu (+|-|*|/|%|stop): ")    
    
    if menu == "+":
        g_int_angka1 = int(input("Masukkan Angka 1: "))
        g_int_angka2 = int(input("Masukkan Angka 2: "))
        g_int_hasil = fg_int_tambah(g_int_angka1, g_int_angka2)
    
    elif menu == "-":
        g_int_angka1 = int(input("Masukkan Angka 1: "))
        g_int_angka2 = int(input("Masukkan Angka 2: "))
        g_int_hasil = fg_int_kurang(g_int_angka1, g_int_angka2)    
    
    elif menu == "*":
        g_int_angka1 = int(input("Masukkan Angka 1: "))
        g_int_angka2 = int(input("Masukkan Angka 2: "))
        g_int_hasil = fg_int_kali(g_int_angka1, g_int_angka2)    
    
    elif menu == "/":
        g_int_angka1 = int(input("Masukkan Angka 1: "))
        g_int_angka2 = int(input("Masukkan Angka 2: "))
        g_int_hasil = fg_int_bagi(g_int_angka1, g_int_angka2)    
    
    elif menu == "stop":
        print("Terima kasih telah menggunakan program.")
        break  
    
    else:
        g_int_hasil = "Operasi tidak valid"
    
    print(f"Hasil: {g_int_hasil}")
    
