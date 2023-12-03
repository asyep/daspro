#Nama   : Asep Nadhirin
#NIM    : 2308165
#Kelas  : RPL-1A


import  time
start_time = time.time()

#Binary Search Function
def binarySearch(array, cariNilai):
    indexLow, indexHigh = 0, len(array) - 1 #Menentukan index pertama (selalu 0) dan index terakhirnya (n - 1)
    
    while indexLow  <= indexHigh:
        middle = (indexLow + indexHigh) // 2    #untuk membagi 2 elemen array
        middleValue = array[middle]
        
        if middleValue == cariNilai:
            return middle   #index elemen yang ditemukan
        elif middleValue < cariNilai:
            indexLow = middle + 1
        else:
            indexHigh = middle - 1
    return -1   #jika elemen tidak ditemukan

array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]
cari = 60
result = binarySearch(array, cari)

if (result != -1):
    print(f"Nilai {cari} ditemukan pada index ke-{result}")
else:
    print(f"Nilai {cari} tidak ditemukan dalam array")
    
print(f'Execution time Binary Search: {time.time() - start_time }')