angka = int(input("Masukkan bilangan bulat (>=0): "))

if angka < 0:
    print("Bilangan harus >= 0!")
else:
    biner = bin(angka).replace("0b", "")
    print(f"Bilangan {angka} dalam biner adalah: {biner}")