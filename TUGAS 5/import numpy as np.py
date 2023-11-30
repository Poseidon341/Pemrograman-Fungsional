import matplotlib.pyplot as plt
import numpy as np

# Buat data titik-titik
xpoints = np.array([0, 6])
ypoints = np.array([0, 10])

# Plot garis
plt.plot(xpoints, ypoints, marker='^', linestyle='-', color='b', label='Garis')


xpoints = np.array([1, 8, 10])
ypoints = np.array([4, 10, 5])


plt.figure(figsize=(8, 6))

# Plot garis
plt.plot(xpoints, ypoints, marker='o', linestyle='-', color='red', label='Garis')

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([2, 5, 8, 11])


# Membuat plot untuk garis y1 dan y2
plt.plot(y1, label='Garis 1', marker='o', linestyle='--', color='blue')
plt.plot(y2, label='Garis 2', marker='s', linestyle='--', color='green')
plt.plot(y3, label='Garis 3', marker='^', linestyle='--', color='red')

# Menambahkan judul dan label sumbu
plt.title('Plot 3 Garis')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Atur label dan judul
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Contoh Plot Garis')

# Data titik-titik
x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

# Membuat scatter plot
plt.scatter(x, y, color='red', marker='^', label='Data Points')

# Menambahkan judul dan label sumbu
plt.title('Scatter Plot')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Tampilkan grid
plt.grid(True)

# Tampilkan legenda
plt.legend()

# Tampilkan plot
plt.show()

