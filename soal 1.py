opening = "Selamat datang di Soal 1 Penugasan 7 tentang String"
c = opening.center(90 , '=')
print(c)

def fungsistring(kata) :
    print("\nKata dalam kondisi awal : ", kata)
    print("\n(",kata,") setelah diberi fungsi capitalize menjadi")
    a = kata.capitalize()
    print(a)
    print("\n(",kata,") setelah diberi fungsi endswith menjadi")
    print(kata.endswith('World'))
    print("\n(",kata,") setelah diberi fungsi upper dan lower menjadi")
    u = kata.upper()
    l = kata.lower()
    print(u)
    print(l)
katakata = input('Masukkan kata-kata yang ingin diolah :')
fungsistring(katakata)