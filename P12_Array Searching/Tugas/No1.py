#Nama   : Asep Nadhirin
#NIM    : 2308165
#Kelas  : RPL-1A


#Linear Search Function
def LinearSearch(array, cariBarang):
    for i in range (len(array)):
        if array [i] == cariBarang:
            return i    #index elemen yang ditemukan 
    return -1   #jika elemen tidak ditemukan

array = ["Beras", "Gula", "Minyak goreng", "Tepung terigu", "Telur", "Sabun mandi", "Shampoo", "Sarden", "Mi instan", "Kecap", "Garam", "Susu kental manis", "Kopi bubuk", "Mie instan", "Teh celup"]
Barang = input("Barang apa yang ingin dicari: ")
result = LinearSearch(array, Barang)

if (result != -1):
    print(f"Barang {Barang} tersedia di toko")
else :
    print(f"Barang {Barang} tidak tersedia di toko")
