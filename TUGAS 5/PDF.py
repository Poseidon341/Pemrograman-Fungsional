'''
from matplotlib import pyplot as plt
# Mengimpor fungsi normal dari pustaka numpy.random
# Digunakan untuk menghasilkan sampel data dari distribusi normal
from numpy.random import normal
# Mengimpor fungsi mean dan std dari pustaka numpy
# Digunakan untuk menghitung rata-rata dan standar deviasi data
from numpy import mean, std
# Mengimpor distribusi normal dari pustaka scipy.stats
# Digunakan untuk analisis statistik terkait distribusi normal
from scipy.stats import norm

# Menghasilkan sampel data dari distribusi normal
sample = np.random.normal(size=1000)

# Membuat histogram
plt.hist(sample, bins=10, color='skyblue', edgecolor='black')

# Menambahkan judul dan label sumbu
plt.title('Histogram Distribusi Normal')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')

# Menampilkan plot
plt.show() 
'''

'''

from matplotlib import pyplot as plt
import numpy as np  # Menambahkan import numpy as np

# Menghasilkan sampel data dari distribusi normal
sample = np.random.normal(size=1000)

# Membuat histogram
plt.hist(sample, bins=10, color='skyblue', edgecolor='black')
'''
'''
from matplotlib import pyplot as plt
import numpy as np  # Menambahkan import numpy as np

# Menghasilkan sampel data dari distribusi normal
sample = np.random.normal(size=1000)

# Membuat histogram
plt.hist(sample, bins=4, color='skyblue', edgecolor='black')

# Menambahkan judul dan label sumbu
plt.title('Histogram Distribusi Normal')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')

# Menampilkan plot
plt.show()
'''
'''
from matplotlib import pyplot as plt
import numpy as np  # Menambahkan import numpy as np

# Cara membuat sample data
sample = np.random.normal(loc=50, scale=5, size=1000)

# Panggil variabel sample untuk mengetahui hasilnya:
# print(sample)  # Uncomment jika ingin melihat hasil sampel

# Tampilkan dalam bentuk histogram
plt.figure(figsize=(5, 4))  # Perkecil media gambar
plt.hist(sample, bins=10, density=True, color='skyblue', edgecolor='black')

# Menambahkan judul dan label sumbu
plt.title('Histogram Distribusi Normal')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')

# Menampilkan plot
plt.show()
'''

'''
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

# Menghasilkan sampel data dari distribusi normal
sample = np.random.normal(size=1000)

# Menghitung rata-rata dan standar deviasi dari sampel
sample_mean = np.mean(sample)
sample_std = np.std(sample)

# Menampilkan rata-rata dan standar deviasi
print('Mean=%.3f\nStandard Deviation=%.3f' % (sample_mean, sample_std))

# Menentukan distribusi normal dengan rata-rata dan standar deviasi di atas
dist = norm(sample_mean, sample_std)

# Menampilkan distribusi normal yang ditentukan
print(dist)
'''
'''
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

# Menghasilkan sampel data dari distribusi normal
sample = np.random.normal(size=1000)

# Menghitung rata-rata dan standar deviasi dari sampel
sample_mean = np.mean(sample)
sample_std = np.std(sample)

# Menampilkan rata-rata dan standar deviasi
print('Mean=%.3f\nStandard Deviation=%.3f' % (sample_mean, sample_std))

# Menentukan distribusi normal dengan rata-rata dan standar deviasi di atas
dist = norm(sample_mean, sample_std)

# Menampilkan distribusi normal yang ditentukan
print(dist)

# Membuat list nilai yang akan digunakan dalam perhitungan
values = [value for value in range(30, 70)]

# Menghitung probabilitas menggunakan metode pdf pada distribusi normal
probabilitas = [dist.pdf(value) for value in values]

# Menampilkan hasil probabilitas
print(probabilitas)
'''

'''
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

# Cara membuat sample data dari distribusi normal
sample = norm(loc=50, scale=5).rvs(size=1000)

# Panggil variabel sample untuk mengetahui hasilnya
# atau tampilkan dalam bentuk histogram
plt.figure(figsize=(5, 4))  # Perkecil media gambar
plt.hist(sample, bins=10, density=True)
plt.show()

# Untuk melakukan estimasi parametrik, asumsikan bahwa kita tidak mengetahui distribusi sampel ini.
# Hal pertama yang perlu kita lakukan dengan sampel adalah mengasumsikan distribusinya.
# Mari kita asumsikan distribusi normal. Parameter yang berhubungan dengan distribusi normal adalah
# mean dan standar deviasi (std) untuk menghitung rata-rata dan standar deviasi sebuah sampel.

sample_mean = np.mean(sample)
sample_std = np.std(sample)
print('Mean=%.3f\nStandard Deviation=%.3f' % (sample_mean, sample_std))

# Tentukan distribusi normal dengan rata-rata dan standar deviasi di atas
dist = norm(sample_mean, sample_std)
print(dist)

# Temukan distribusi probabilitas untuk distribusi yang telah ditentukan
# Pertama, buat list nilai yang akan digunakan dalam perhitungan
values = [value for value in range(30, 70)]  # Menggunakan list comprehension

# Manfaatkan list comprehension untuk menerapkan metode pdf
# Berdasarkan value (yang telah disiapkan sebelumnya) pada data dist
probabilitas = [dist.pdf(value) for value in values]

# Panggil variabel probabilitas untuk mengetahui hasilnya
print(probabilitas)

# Plot histogram dari sampel data
plt.hist(sample, bins=10, density=True, alpha=0.5, color='skyblue', edgecolor='black', label='Sample Data')

# Plot distribusi probabilitas yang ditentukan
plt.plot(values, probabilitas, color='red', label='Probability Distribution')

# Menambahkan judul dan label sumbu
plt.title('Histogram dan Distribusi Probabilitas')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi dan Probabilitas')

# Menampilkan legenda
plt.legend()

# Menampilkan plot
plt.show()
'''

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


sample = np.random.normal(loc=50, scale=5, size=1000)

plt.figure(figsize=(8, 6))
plt.hist(sample, bins=10, density=True, alpha=0.7, label='Sample Data')  
plt.xlabel('Nilai')
plt.ylabel('Frekuensi Normalized')


sample_mean = np.mean(sample)
sample_std = np.std(sample)


dist = norm(sample_mean, sample_std)


values = [value for value in range(30, 70)]


probabilitas = [dist.pdf(value) for value in values]


plt.plot(values, probabilitas, label='Distribusi Normal', color='red', linewidth=2)


print('Mean=%.3f\nStandard Deviation=%.3f' % (sample_mean, sample_std))
print("\nNilai Probabilitas:")
for value, prob in zip(values, probabilitas):
    print(f"Nilai: {value}, Probabilitas: {prob:.4f}")

# Menambahkan legenda
plt.legend()

plt.show()