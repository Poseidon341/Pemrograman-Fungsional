'''
# TUGAS 1


def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def tree(expression_tree):
    if isinstance(expression_tree, tuple):
        operator = expression_tree[1]
        left_operand = expression_tree[0]
        right_operand = expression_tree[2]
        
        if operator == '+':
            return add(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))
    else:
        return expression_tree

expression_tree = (((2, '+', 3),), ((5, '-', 1),))

for expression in expression_tree:
    result = tree(expression[0])
    print("Hasil evaluasi ekspresi adalah:", result)

'''

random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_dict = {}
float_tuple = ()
string_list = []

for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        int_dict[item] = {'satuan': satuan, 'puluhan': puluhan, 'ratusan': ratusan}
    elif isinstance(item, float):
        # data float dalam bentuk tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # data string dalam list
        string_list.append(item)

print("Data Integer dalam Dictionary:")
print(int_dict)
print("Data Float dalam Tuple:")
print(float_tuple)
print("Data String dalam List:")
print(string_list)
print(type(float_tuple))

'''

def hitung_nilai_akhir(uts, uas):
    nilai_akhir = 0.4 * uts + 0.6 * uas
    return nilai_akhir


def hitung_nilai_semua_mahasiswa(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        'Mahasiswa1': {'uts': 85, 'uas': 90},
        'Mahasiswa2': {'uts': 70, 'uas': 75},
        'Mahasiswa3': {'uts': 95, 'uas': 88},
        # Tambahkan data mahasiswa lainnya sesuai kebutuhan
    }

    data_nilai_akhir = hitung_nilai_semua_mahasiswa(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()

'''
