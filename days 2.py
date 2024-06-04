# list
# Membuat list
list_buah = ["apel", "pisang", "jeruk"]
# Mengakses list dengan indeks
print(list_buah[0])  # Output apel
print(list_buah[1])  # Output pisang
print(list_buah[2])  # Output jeruk
# Mengubah list
list_buah[1] = "mangga"
print(list_buah)  # Output ['apel', 'mangga', 'jeruk']
# Menambahkan list
list_buah.append("anggur")
print(list_buah)  # Output ['apel', 'mangga', 'jeruk', 'anggur']

# Set
# membuat set
set_buah = {"apel", "pisang", "jeruk"}
# Memeriksa apakah buah ada di set
print("apel" in set_buah)  # Output True
print("mangga" in set_buah)  # Output False
# Menghapus elemen set
set_buah.remove("jeruk")
print(set_buah)  # Output {'apel', 'pisang'}
# Menggabungkan dua set
set_buah2 = {"mangga", "anggur"}
set_buah.update(set_buah2)
print(set_buah)  # Output {'apel', 'pisang', 'mangga', 'anggur'}

#Tuple
# Membuat tuple
tuple_buah = ("apel", "pisang", "jeruk")
# Mengakses tuple dengan indeks
print(tuple_buah[0])  # Output apel
print(tuple_buah[1])  # Output pisang
print(tuple_buah[2])  # Output jeruk
# Tuple tidak bisa diubah setelah dibuat
# Menggabungkan dua tuple
tuple_buah2 = ("mangga", "anggur")
tuple_buah3 = tuple_buah + tuple_buah2
print(tuple_buah3)  # Output ('apel', 'pisang', 'jeruk', 'mangga', 'anggur')