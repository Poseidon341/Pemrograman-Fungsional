random_list = [3.1, 2.7, 'Hello', 5.5, 'Python', 'world', 1, 'AI', 73, 42]

# Memisahkan nilai float, int, dan string menggunakan filter
data_float = list(filter(lambda x: isinstance(x, float), random_list))
data_int = list(filter(lambda x: isinstance(x, int), random_list))
data_string = list(filter(lambda x: isinstance(x, str), random_list))

# Membuat fungsi untuk mengubah nilai int menjadi satuan, puluhan, dan ratusan
def map_int_to_units(num):
    ratusan = num // 100
    puluhan = (num // 10) % 10
    satuan = num % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

# Menggunakan map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
data_int_mapped = list(map(map_int_to_units, data_int))

# Menampilkan hasil
print("Data Float:")
print(data_float)
print("Data Int:")
for item in data_int_mapped:
    print(item)
print("Data String:")
print(data_string)