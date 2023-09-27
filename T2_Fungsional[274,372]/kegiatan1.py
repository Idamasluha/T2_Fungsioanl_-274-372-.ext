my_list = []

# Menambahkan elemen ke dalam list
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Menampilkan isi list
print("Isi list:", my_list)

# Mengakses elemen berdasarkan indeks
print("Elemen pertama:", my_list[0])
print("Elemen kedua:", my_list[1])
print("Elemen ketiga:", my_list[2])

# Menghitung jumlah elemen dalam list
jumlah_elemen = len(my_list)
print("Jumlah elemen dalam list:", jumlah_elemen)

# Mengubah nilai elemen dalam list
my_list[1] = 25
print("Setelah diubah:", my_list)

# Menghapus elemen dari list
my_list.remove(30)
print("Setelah menghapus 30:", my_list)

# Menyisipkan elemen pada indeks tertentu
my_list.insert(1, 15)
print("Setelah menyisipkan 15 pada indeks 1:", my_list)