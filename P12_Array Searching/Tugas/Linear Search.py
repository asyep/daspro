#Nama   : Asep Nadhirin
#NIM    : 2308165
#Kelas  : RPL-1A


import  time
start_time = time.time()

#Linear Search Function
def LinearSearch(array,cariNilai):
    for i in range (len(array)):
        if array [i] == cariNilai:
            return i    #index elemen yang ditemukan
    return -1   #jika elemen tidak ditemukan

array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]
nilai = 60
result = LinearSearch(array, nilai)

if (result != -1):
    print (f"Nilai {nilai} ditemukan pada index ke-{result}")
else:
    print(f"Nilai {nilai} tidak ditemukan dalam array")
    
print(f'Execution time Linear Search: {time.time() - start_time }')