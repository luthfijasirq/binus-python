# Program Konversi Suhu

def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def celcius_ke_kelvin(celcius):
    return celcius + 273.15

def fahrenheit_ke_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_ke_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_ke_celcius(kelvin):
    return kelvin - 273.15

def kelvin_ke_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Program Konversi Suhu")
    print("1. Celcius ke Fahrenheit")
    print("2. Celcius ke Kelvin")
    print("3. Fahrenheit ke Celcius")
    print("4. Fahrenheit ke Kelvin")
    print("5. Kelvin ke Celcius")
    print("6. Kelvin ke Fahrenheit")

    choice = int(input("Masukkan nomor konversi yang ingin Anda lakukan: "))

    if choice == 1:
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        print(f"{celcius}°C = {celcius_ke_fahrenheit(celcius)}°F")
    elif choice == 2:
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        print(f"{celcius}°C = {celcius_ke_kelvin(celcius)}K")
    elif choice == 3:
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_ke_celcius(fahrenheit)}°C")
    elif choice == 4:
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_ke_kelvin(fahrenheit)}K")
    elif choice == 5:
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        print(f"{kelvin}K = {kelvin_ke_celcius(kelvin)}°C")
    elif choice == 6:
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        print(f"{kelvin}K = {kelvin_ke_fahrenheit(kelvin)}°F")
    else:
        print("Pilihan tidak valid. Silakan masukkan nomor yang valid.")

if __name__ == "__main__":
    main()
