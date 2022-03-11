def persegi():
    s = float(input("\nMasukan Panjang Sisi: "))
    luasP = s**2
    print("\nLuas Persegi \t\t:",luasP)
    print("\nLuas Persegi \t\t:{}".format(luasP))
    print(F"\nLuas Persegi \t\t:",(luasP))
    print( ' ' )

def persegipanjang():
    panjang = float(input("\nMasukan Panjang: "))
    lebar = float(input("Masukan Lebar: "))
    luasPP = panjang*lebar
    print("\nLuas Persegi Panjang \t\t:",luasPP)
    print("\nLuas Persegi Panjang \t\t:{}".format(luasPP))
    print(F"\nLuas Persegi Panjang \t\t:",(luasPP))
    print( ' ' )

def segitiga():
    alas= float(input('masukkan alas segitiga : '))
    tinggi= float(input('masukkan tinggi segitiga :'))
    hasil=0.5*alas*tinggi
    print (' luas segitiganya adalah : ', hasil, 'cm')
    print (' luas segitiganya adalah : {}'.format(hasil), 'cm')
    print (F' luas segitiganya adalah : {hasil} cm')
    print( ' ' )

def jajargenjang():
    alas = float(input("Masukan alas jajargenjang: "))
    tinggi = float(input("Masukan tinggi jajargenjang: "))
    luasJG = alas * tinggi
    print("Luas Jajargenjang : ", luasJG)
    print("Luas Jajargenjang : {}".format(luasJG))
    print(F"Luas Jajargenjang : ", (luasJG))
    print( ' ' )

def trapesium():
    a = float(input(" Masukan Panjang Sisi Atas: "))
    s = float(input("Masukan Panjang Sisi Bawah: "))
    t = float(input("Masukang Tinggi: "))
    luasT=(((a+s)/2)*t)

    print("Luas bangun trapesium : ", luasT)
    print("Luas bangun trapesium : {}".format(luasT))
    print(F"Luas bangun trapesium : ", (luasT))
    print( ' ' )

def lingkaran():
    phi = 3.14
    rLinkarang = float(input("Masukkan panjang jari-jari lingkaran: "))
    luasLingkaran = phi*rLinkarang*rLinkarang
    print("Luas lingkaran adalah : "+ str(luasLingkaran))
    print("Luas lingkaran adalah : {}".format(luasLingkaran))
    print(F"Luas lingkaran adalah : "+ str(luasLingkaran))
    print( ' ' )

while True:
    print("KALKULATOR HITUNG LUAS BANGUN RUANG")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Jajar Genjang")
    print("5. Trapesium")
    print("6. Lingkaran")
    pilih = input("Pilihan 1-6 : ")
    if pilih == "1":
        persegi()
    elif pilih == "2":
        persegipanjang()
    elif pilih == "3":
        segitiga()
    elif pilih == "4":
        jajargenjang()
    elif pilih == "5":
        trapesium()
    elif pilih == "6":
        lingkaran()
    else:
        print("Keyword Anda salah coba ulang lagi!!!")