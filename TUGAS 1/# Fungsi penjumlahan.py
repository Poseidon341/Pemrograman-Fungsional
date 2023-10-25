# Fungsi penjumlahan
def add(a, b):
    return a + b

# Fungsi pengurangan
def minus(a, b):
    return a - b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi pembagian
def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Fungsi tree yang menerima pohon ekspresi
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

# Contoh pohon ekspresi: (2+3) (5-1)
expression_tree = ((2, '+', 3), (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

# Mencetak hasil evaluasi ekspresi
print("Hasil evaluasi ekspresi adalah:", result)
