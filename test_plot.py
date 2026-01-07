import matplotlib.pyplot as plt
import random

# 1. SIAPKAN GELAS DAN TINTA
langkah = 100
x, y = 10, 10  # Titik tengah gelas

jejak_x = [x]
jejak_y = [y]

# 2. PROSES TINTA MENYEBAR (DIFUSI)
for _ in range(langkah):
    # Tinta terdorong ke arah acak
    x += random.choice([-1, 0, 1])
    y += random.choice([-1, 0, 1])

    # Pastikan tinta tidak keluar dari dinding gelas (0-19)
    x = max(0, min(19, x))
    y = max(0, min(19, y))

    jejak_x.append(x)
    jejak_y.append(y)

# 3. GAMBAR HASILNYA
plt.figure(figsize=(7, 5))

# Buat titik-titik tinta dengan gradasi warna biru
plt.scatter(jejak_x, jejak_y, c=range(len(jejak_x)), cmap='Blues', edgecolors='black')

# Tandai tempat tinta pertama kali jatuh dengan simbol X merah
plt.scatter(10, 10, color='red', marker='X', s=100, label="Tinta Jatuh")

plt.title("Simulasi Tetesan Tinta di Air")
plt.colorbar(label="Waktu Menyebar")
plt.legend()
plt.show()