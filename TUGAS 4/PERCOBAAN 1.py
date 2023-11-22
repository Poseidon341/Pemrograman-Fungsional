

# Higher-Order Function (HOF)
def perkalian(a, b):
    return a * b

result_hof = perkalian(2, 3)
print(result_hof)

# Currying
def curry_function(a):
    def dengan(b):
        return a * b
    return dengan

result_currying = curry_function(2)(3)
print(result_currying)




def uppercase_decorator(func): 
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())





def title_decorator(func):
    def wrapper():
        result = func()
        make_title = result.title()
        print(make_title + " - Data is converted to title case")
        return make_title
    return wrapper

def split_string_decorator(func):
    def wrapper():
        result = func()
        splitted_string = result.split()
        print(str(splitted_string) + " - Then Data is splitted")
        return splitted_string
    return wrapper

@split_string_decorator
@title_decorator
def say_hi():
    return 'hello there'

say_hi()





def translasi(tx, ty):
    def transformasi(p):
        x, y = p
        return x + tx, y + ty
    return transformasi

def dilatasi(sx, sy):
    def transformasi(p):
        x, y = p
        return x * sx, y * sy
    return transformasi

def rotasi(sudut):
    import math
    def transformasi(p):
        x, y = p
        x_baru = x * math.cos(math.radians(sudut)) - y * math.sin(math.radians(sudut))
        y_baru = x * math.sin(math.radians(sudut)) + y * math.cos(math.radians(sudut))
        return x_baru, y_baru
    return transformasi

titik = (3, 5)

translasi_2_minus_1 = translasi(2, -1)
dilatasi_2_minus_1 = dilatasi(2, -1)
rotasi_30_degrees = rotasi(30)

titik_setelah_translasi = translasi_2_minus_1(titik)
titik_setelah_dilatasi = dilatasi_2_minus_1(titik)
titik_setelah_rotasi = rotasi_30_degrees(titik)

print("Koordinat setelah translasi:", titik_setelah_translasi)
print("Koordinat setelah dilatasi:", titik_setelah_dilatasi)
print("Koordinat setelah rotasi:", titik_setelah_rotasi)




def point(x, y):
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

    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 3), point(6, 2)))  # ubah nilai input dengan 4 digit nim akhir kalian




def point(x, y):
    return x, y

def line_equation_of(p, m):
    x, y = p

    def calculate_c(x, y, m):
        return y - m * x

    C = calculate_c(x, y, m)

    return f"y = {m:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (3,6) dan bergradien 2:")
print(line_equation_of(point(3, 6), 2))  # ubah nilai input dengan 3 digit nim akhir kalian





