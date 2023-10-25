

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


# Fungsi untuk mengkonversi data
# Fungsi untuk mengkonversi data
def konversi_data(data):
    hasil_konversi = []
    for item in data:
        # Split data untuk mendapatkan minggu, hari, jam, dan menit
        parts = item.split()
        minggu = int(parts[0])
        hari = int(parts[2])
        jam = int(parts[4])
        menit = int(parts[6])
        # Menggunakan currying untuk mengkonversi
        konvert = konversi()(menit)(jam)(hari)(minggu)
        hasil_konversi.append(konvert)
    return hasil_konversi

output = konversi_data(data)
print("output =", output)





