#Nama   : Asep Nadhirin
#NIM    : 2308165
#Kelas  : RPL-1A


#Linear Search Function
def LinearSearch(array, cariNama):
    for i in range (len(array)):
        if array [i] == cariNama:
            return i    #index elemen yang ditemukan
    return -1   #jika elemen tidak ditemukan

array = ["ACHMAD SOEWARDI", "AKHMAD ALWAN RABBANI", "ANDIKA EKA KURNIA", "ARIEL JULIANS", "ASEP NADHIRIN", "BAGAS ADHI NUGRAHA", "BANU ARIEF MUZAKI", "FATRA AL KHAWARIZMI", "FAUZIAH ZAHRA", "GHAISAN DAFFA AL FAYADH", "GREGORIUS CHRISTIAN SUNARYO", "HARYO WICAKSONO", "MARYAM SILVA RAHAYU", "MUHAMAD SHANDY WINATA", "MUHAMMAD AIMAN ZIKRI ZEGA", "MUHAMMAD FADHEL RAIHAN", "MUHAMMAD NASHIRUL HAQ RESA", "MUHAMMAD PADLI SEPTIANA", "MUHAMMAD RAFI ZAMZAMI", "MUTIA YASINTA"]
nama = input("Masukan nama yang ingin dicari: ")
result = LinearSearch(array, nama)

if (result != -1):
    print(f"Mahasiswa dengan nama {nama} terdata sebagai mahasiswa prodi RPL")
else :
    print(f"Mahasiswa dengan nama {nama} tidak terdata sebagai mahasiswa prodi RPL")