def konversi(j=0):
    def menit(m=0):
        def jam(h=0):
            def hari(d=0):
                def minggu(w=0):
                    return (((w * 7 + d) * 24 + h) * 60 + m)
                return minggu
            return hari
        return jam
    return menit

# Data input
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi untuk mengambil nilai integer dari setiap data
def ambil_integer(data):
    # Split data untuk mendapatkan semua kata
    kata_kata = data.split()
    # Gunakan filter dan str.isdigit() untuk mengambil nilai integer
    nilai_integer = list(filter(str.isdigit, kata_kata))
    return nilai_integer

# Gunakan list comprehension untuk mendapatkan nilai integer dari setiap data
output = [ambil_integer(item) for item in data]

# Print hasilnya
for item in output:
    print(item)