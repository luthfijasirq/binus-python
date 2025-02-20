usia= int(input("Masukkan umur:"))

if ( ( usia > 0 ) and ( usia <= 1 ) ):
    print("Bayi")
elif ( ( usia >= 2 ) and ( usia <= 3 ) ):
    print("Balita")
elif ( ( usia > 4 ) and ( usia <= 5 ) ):
    print("Anak prasekolah")
elif ( ( usia >= 6 ) and ( usia <= 12 ) ):
    print("Anak")
elif ( ( usia >= 13 ) and ( usia <= 17 ) ):
    print("Remaja") 
elif ( ( usia >= 18 ) and ( usia <= 21 ) ):
    print("Dewasa muda")  
elif ( ( usia >= 22 ) and ( usia <= 30 ) ):
    print("Pra-Dewasa") 
elif ( ( usia >= 31 ) and ( usia <= 50 ) ):
    print("Dewasa")   
elif ( ( usia >= 51 ) and ( usia <= 70 ) ):
    print("pra-lansia") 
elif ( ( usia >= 71 ) ):
    print("Lansia")      
else:
    print("Bayi")
