# Membuat dictionary
my_dict = {
    'nama': 'John',
    'usia': 30,
    'pekerjaan': 'Programmer'
}

# Mengakses nilai berdasarkan kunci
print("Nama:", my_dict['nama'])
print("Usia:", my_dict['usia'])

# Mengembalikan daftar kunci dalam dictionary
kunci = my_dict.keys()
print("Kunci dalam dictionary:", list(kunci))

# Mengembalikan daftar nilai dalam dictionary
nilai = my_dict.values()
print("Nilai dalam dictionary:", list(nilai))

# Mengembalikan daftar pasangan kunci-nilai dalam dictionary
pasangan = my_dict.items()
print("Pasangan kunci-nilai dalam dictionary:", list(pasangan))

# Menambahkan pasangan kunci-nilai baru
my_dict['alamat'] = 'Jl. Contoh No. 123'

# Menghapus kunci tertentu dari dictionary
if 'pekerjaan' in my_dict:
    del my_dict['pekerjaan']

# Menggabungkan dictionary dengan dictionary lain
other_dict = {'hobi': 'Renang'}
my_dict.update(other_dict)

# Menghapus dan mengembalikan pasangan kunci-nilai terakhir dari dictionary
last_item = my_dict.popitem()

# Menghapus semua pasangan kunci-nilai dari dictionary
my_dict.clear()