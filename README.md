---

# 💧 Simulasi Difusi Tetesan Tinta — Visualisasi Algoritma Random Walk

### 📘 Mata Kuliah: Strategi Algoritma

### 👥 Kelompok 4

---

## 📖 Latar Belakang Singkat

Pernahkah Anda memperhatikan bagaimana setetes tinta menyebar di dalam segelas air? Pergerakan tersebut tampak kacau, namun mengikuti prinsip matematika yang disebut **Random Walk** (Gerak Acak).

Dalam proyek ini, kami menggunakan **Algoritma Random Walk** untuk mensimulasikan fenomena difusi. Setiap titik warna mewakili molekul tinta yang bergerak secara acak akibat tabrakan dengan molekul air. Simulasi ini membantu kita memahami bagaimana probabilitas dan langkah-langkah kecil yang tidak teratur dapat membentuk pola penyebaran yang luas seiring berjalannya waktu.

---

## 🖼️ Visualisasi Simulasi

Berikut adalah perbandingan antara konsep dasar koordinat dan hasil simulasi penyebaran tinta:

| Konsep Dasar (Plot Garis) | Hasil Simulasi (Scatter Plot) |
| --- | --- |
| ![Grafik Garis](https://github.com/user-attachments/assets/f15cd2db-8552-4645-8c91-eef49c760121) | ![Grafik Scatter](https://github.com/user-attachments/assets/8f089b45-a8bf-4a82-a750-d68b9e01471d) |
| **Grafik Linear**: Menunjukkan dasar pemetaan koordinat  dan  sebelum algoritma acak diterapkan. | **Scatter Plot Difusi**: Menunjukkan jejak molekul tinta. Warna ungu (awal) ke kuning (akhir) menunjukkan urutan waktu penyebaran. |

---

## ⚙️ Model Algoritma Random Walk

Dalam simulasi tetesan tinta ini:

* **Titik Awal (Bintang Merah)**: Lokasi tepat saat tinta menyentuh air (koordinat 10,10).
* **Langkah Acak**: Menggunakan fungsi `random.choice([-1, 0, 1])` untuk menentukan arah gerakan molekul ke segala arah.
* **Dinding Gelas**: Batasan area  yang memastikan molekul tetap berada dalam wadah simulasi.
* **Gradasi Warna (Viridis)**: Merepresentasikan **Urutan Waktu**. Semakin kuning warnanya, semakin baru posisi tersebut dikunjungi oleh molekul tinta.

Implementasi dilakukan dengan **Python** dan pustaka **Matplotlib** untuk menghasilkan visualisasi yang presisi dan mudah dipahami.

---

## 🚀 Manfaat Simulasi

✅ Mempermudah pemahaman konsep **Probabilitas dan Stokastik**.

✅ Visualisasi nyata dari fenomena fisika **Difusi Molekul**.

✅ Dasar pengembangan algoritma untuk **Machine Learning** dan **Simulasi Ekonomi**.

✅ Membantu analisis data spasial yang memiliki unsur ketidakpastian.

---

## 👥 Anggota Kelompok 4

| Nama | Asal Universitas | Peran |
| --- | --- | --- |
| **Muhammad Rafli Nurfathan** | University Bhinneka Nusantara | Perancang & Penulis Utama |
| **Rachmat Robby Pratama** | University Bhinneka Nusantara | Analisis & Kode |
| **Daniel Lee Bitzer Anthony** | University Bhinneka Nusantara | Dokumentasi & Review |

---

> ✨ *"Like a drop of ink in water, even the most random paths lead to a beautiful expansion of knowledge."*

---
