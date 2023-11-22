# Nama  : Asep Nadhirin
# NIM   : 2308165
# Kelas : RPL-1A

 
import numpy as np

def nilai_array(low: int, high:int, size: int):
    rng = np.random.default_rng()
    return rng.integers(low=low, high=high, size=size)

nilai_ujian = nilai_array(0, 100, 30)
nilai_ujian.sort()
nilai_sorted = nilai_ujian[::-1]

print(f"Data nilai ujian: {nilai_sorted}")
print(f"Peringkat 5 nilai terbesar: {nilai_sorted[:5]}")