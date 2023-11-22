# Nama  : Asep Nadhirin
# NIM   : 2308165
# Kelas : RPL-1A

import numpy as np

def suhu_array(low: int, high:int, size: int):
    rng = np.random.default_rng()
    return rng.integers(low=low, high=high, size=size)

def Fahrenheit(celcius):
    return 9/5 * celcius + 32


suhu_singapura = suhu_array(-100, 100, 10)

print("Celcius: ", suhu_singapura)
print("Fahrenheit: ", Fahrenheit(suhu_singapura))