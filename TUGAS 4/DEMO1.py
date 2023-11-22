import math

def translasi_decorator(func):
    def inner(p, tx, ty):
        x, y = func(p)
        return x + tx, y + ty
    return inner

def dilatasi_decorator(func):
    def inner(p, sx, sy):
        x, y = func(p)
        return x * sx, y * sy
    return inner

def rotasi_decorator(func):
    def inner(p, sudut):
        x, y = func(p)
        x_baru = x * math.cos(math.radians(sudut)) - y * math.sin(math.radians(sudut))
        y_baru = x * math.sin(math.radians(sudut)) + y * math.cos(math.radians(sudut))
        return x_baru, y_baru
    return inner


@translasi_decorator
def translasi(p):
    return p

@dilatasi_decorator
def dilatasi(p):
    return p

@rotasi_decorator
def rotasi(p):
    return p

def point_input():
    x = float(input("Masukkan nilai x untuk titik: "))
    y = float(input("Masukkan nilai y untuk titik: "))
    return x, y

def line_equation_of(p1, p2):
    def calculate_m(x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1)

    def calculate_c(x1, y1, m):
        return y1 - m * x1

    x1, y1 = p1
    x2, y2 = p2

    M = calculate_m(x1, y1, x2, y2)
    C = calculate_c(x1, y1, M)

    return f"y = {M:.2f}x + {C:.2f}" if C < 0 else f"y = {M:.2f}x + {C:.2f}"

if __name__ == '__main__':
    # Input dari pengguna untuk titik A dan B
    print("Masukkan koordinat untuk titik A:")
    A = point_input()
    print("Masukkan koordinat untuk titik B:")
    B = point_input()

    # Input untuk translasi, dilatasi, dan rotasi
    tx = float(input("Masukkan nilai translasi tx: "))
    ty = float(input("Masukkan nilai translasi ty: "))
    sudut = float(input("Masukkan nilai rotasi dalam derajat: "))
    sx = float(input("Masukkan faktor skala sx: "))  # Input faktor skala sx
    sy = float(input("Masukkan faktor skala sy: "))  # Input faktor skala sy

    # Lakukan transformasi berurutan pada titik A dan B
    A_transformed = rotasi(translasi(dilatasi(A, sx, sy), tx, ty), sudut)
    B_transformed = rotasi(translasi(dilatasi(B, sx, sy), tx, ty), sudut)

    # Dapatkan persamaan garis dari titik hasil transformasi
    persamaan_garis_AB = line_equation_of(A, B)
    persamaan_garis_transformasi = line_equation_of(A_transformed, B_transformed)

    # Output persamaan garis hasil transformasi
    print("Persamaan garis yang melalui titik A dan B sebelum transformasi:", persamaan_garis_AB)
    print("Persamaan garis baru setelah transformasi:", persamaan_garis_transformasi)

    # Lakukan transformasi dilatasi rotasi dan translatasi pada titik A dan B
    A_dilatasi = dilatasi(A, sx, sy)
    B_dilatasi = dilatasi(B, sx, sy)

    A_translasi = translasi(A_dilatasi, tx, ty)
    B_translasi = translasi(B_dilatasi, tx, ty)

    A_rotasi = rotasi(A_translasi, sudut)
    B_rotasi = rotasi(B_translasi, sudut)

    # Output hasil dari setiap operasi transformasi
    print("\nHasil Dilatasi:")
    print(f"Titik A setelah dilatasi: {A_dilatasi}")
    print(f"Titik B setelah dilatasi: {B_dilatasi}")

    print("\nHasil Translasi:")
    print(f"Titik A setelah translasi: {A_translasi}")
    print(f"Titik B setelah translasi: {B_translasi}")

    print("\nHasil Rotasi:")
    print(f"Titik A setelah rotasi: {A_rotasi}")
    print(f"Titik B setelah rotasi: {B_rotasi}")
