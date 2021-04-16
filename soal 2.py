import random

opening = "Selamat datang di Soal 2 Penugasan 7 tentang Fungsi Numerik"
c = opening.center(90 , '=')
print(c)

import math
import random

def fungsinumerik(angka1,angka2,angka3):
    print('\nMenggunakan fungsi abs dan fabs')
    print(angka1, 'menjadi',abs(angka1))
    print(angka2, 'menjadi',abs(angka2))
    print(angka3, 'menjadi', abs(angka3))
    print(angka1, 'menjadi',math.fabs(angka1))
    print(angka2, 'menjadi',math.fabs(angka2))
    print(angka3, 'menjadi', math.fabs(angka3))
    print('\nMenggunakan fungsi ceil')
    print(angka1, 'menjadi',math.ceil(angka1))
    print(angka2, 'menjadi',math.ceil(angka2))
    print(angka3, 'menjadi', math.ceil(angka3))
    print('\nMenggunakan fungsi floor')
    print(angka1, 'menjadi', math.floor(angka1))
    print(angka2, 'menjadi',math.floor(angka2))
    print(angka3, 'menjadi', math.floor(angka3))
    print('\nMencari nilai Minimal dan Maksimal')
    print('nilai minimal antara ketiganya adalah = ', min(angka1,angka2,angka3))
    print('nilai maksimal antara ketiganya adalah = ', max(angka1,angka2,angka3))
    print('\nMemilih nilai random dengan choice')
    a = [angka1,angka2,angka3]
    print('a= ', a)
    print('random 1')
    print('choice= ', random.choice(a))
    print('random 2')
    print('choice= ', random.choice(a))
    print('random 3')
    print('choice= ', random.choice(a))

print('Gunakan tanda titik untuk menulis desimal')
x = float(input('Masukkan angka pertama: '))
y = float(input('Masukkan angka kedua: '))
z = float(input('Masukkan angka ketiga: '))
fungsinumerik(x,y,z)
