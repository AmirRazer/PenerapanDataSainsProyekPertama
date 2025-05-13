# Proyek Pertama: Menyelesaikan Permasalahan Departemen Human Resources (HR)

### Business Understanding (Latar Belakang Bisnis)

Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000 dengan jumlah karyawan lebih dari 1000 orang yang tersebar di berbagai wilayah Indonesia. Meski tergolong perusahaan besar, Jaya Jaya Maju menghadapi tantangan serius dalam pengelolaan karyawan, terutama terkait tingginya angka **attrition rate** (rasio karyawan keluar terhadap total karyawan) yang telah melebihi 10%.

Tingginya attrition rate ini mengakibatkan ketidakstabilan operasional perusahaan, meningkatnya biaya perekrutan dan pelatihan, serta berkurangnya produktivitas tim. Oleh karena itu, manajer HR membutuhkan bantuan untuk mengidentifikasi faktor-faktor penyebab attrition serta alat bantu untuk memantau kondisi tersebut secara efisien.

---

### Permasalahan Bisnis

Permasalahan bisnis yang ingin diselesaikan dalam proyek ini adalah sebagai berikut:

1. **Tingginya angka attrition rate**, namun tidak diketahui faktor-faktor utamanya.
2. **Ketiadaan business dashboard** yang dapat digunakan HR untuk memantau kondisi karyawan secara real-time dan terstruktur.
3. **Kesulitan dalam pengambilan keputusan strategis** karena tidak adanya insight dari data historis karyawan.
4. **Data karyawan yang belum dimanfaatkan secara optimal** untuk tujuan analisis dan perencanaan sumber daya manusia.

---

### Cakupan Proyek

Cakupan proyek yang akan dikerjakan meliputi:

1. **Eksplorasi dan analisis dataset karyawan** untuk mengidentifikasi pola dan faktor penyebab tingginya attrition rate.
2. **Visualisasi data dan pembuatan dashboard** interaktif yang dapat digunakan oleh tim HR untuk memantau kondisi karyawan dan attrition rate.
3. **Penyusunan insight dan rekomendasi** berbasis data untuk membantu manajer HR dalam membuat keputusan strategis guna mengurangi angka attrition.
4. **Pengelompokan fitur-fitur penting** seperti usia, gaji, lama bekerja, departemen, dan lainnya yang berkontribusi terhadap keputusan karyawan untuk keluar dari perusahaan.

### Persiapan

Sumber data: [Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

<!-- Setup environment:
```

``` -->


## Business Dashboard

Sebagai bagian dari upaya membantu departemen Human Resources (HR) di perusahaan Jaya Jaya Maju, saya telah membuat sebuah **business dashboard interaktif menggunakan Tableau**. Dashboard ini dirancang untuk memudahkan manajer HR dalam memonitor dan menganalisis faktor-faktor yang berkontribusi terhadap tingkat attrition (keluar kerja) di perusahaan.
![image](https://github.com/user-attachments/assets/8d316294-5b2e-4219-84f1-5254926d53f6)

Mockup gambar di atas di gunakan agar mempermudah saat mengklompokan hasil visualisasi dashboard yang telah di buat

![image](https://github.com/user-attachments/assets/0c443cbd-2a71-45af-b5be-4bf7d8493825)

### Fitur dan Visualisasi dalam Dashboard:

1. **Ringkasan Karyawan:**
   Menyajikan informasi umum seperti total karyawan, rata-rata lama bekerja, usia, dan pendapatan bulanan. Semua data ini akan otomatis menyesuaikan tergantung pada filter yang digunakan.

2. **Analisis Gender:**
   Menampilkan perbandingan antara karyawan laki-laki dan perempuan berdasarkan status aktif atau resign.

3. **Status Karyawan (Resign vs Active):**
   Visualisasi dalam bentuk pie chart yang menggambarkan proporsi karyawan yang masih aktif dibandingkan yang telah resign.

4. **Distribusi Berdasarkan Bidang Pendidikan:**
   Treemap yang menunjukkan latar belakang pendidikan karyawan, membantu melihat apakah terdapat hubungan antara bidang pendidikan dan keputusan untuk resign.

5. **Attrition Berdasarkan Education:**
   Bar chart untuk melihat tingkat attrition berdasarkan jenis pendidikan, sebagai acuan dalam menentukan strategi rekrutmen ke depan.

6. **Pendapatan Berdasarkan Job Role:**
   Menampilkan perbandingan antara rata-rata pendapatan bulanan dan *monthly rate* berdasarkan peran pekerjaan.

### Tujuan Dashboard:
- Mengidentifikasi pola dan faktor utama yang memengaruhi keputusan resign.
- Menyediakan tampilan visual yang interaktif dan mudah dipahami.
- Membantu HR dalam pengambilan keputusan strategis berbasis data.

### Tools yang Digunakan:
- **Tableau** sebagai platform untuk membangun dashboard interaktif dan responsif.

> **Link Akses Dashboard**: [Lihat di Tableau Public](https://public.tableau.com/app/profile/amir.mahmud4793/viz/ProyekPertamaDicodingDs/Dashboard1)

> **Catatan**: Dashboard bersifat dinamis dan akan berubah secara otomatis sesuai dengan filter atau interaksi pengguna.

> **Video**: [Lihat Video](https://youtu.be/JH7vlu0xquo)



## Menjalankan Sistem Machine Learning

Untuk menjalankan prototype sistem machine learning yang telah dibuat, ikuti langkah-langkah berikut ini:
> **Link Akses Dashboard**: [Lihat di StreamlitOnline](https://amirrazer-penerapandatasainsproyekpertama-app-9nb4yz.streamlit.app/)

![image](https://github.com/user-attachments/assets/c880d5ae-8b04-4b74-96b9-e4ea3f261093)
dengan prototype machine learning ini perusahaan dapat **meningkatkan retensi karyawan, mengurangi biaya rekrutmen, serta menciptakan lingkungan kerja yang lebih stabil dan produktif.**

Untuk menjalankan proyek HR Analytics ini secara lokal, silakan ikuti panduan berikut:

### 🔗 Repository
Proyek ini tersedia di GitHub:  
👉 [PenerapanDataSainsProyekPertama](https://github.com/AmirRazer/PenerapanDataSainsProyekPertama)

---

### 1. Clone Repository

Clone repositori ke komputer lokal Anda menggunakan perintah berikut:

```bash
git clone https://github.com/AmirRazer/PenerapanDataSainsProyekPertama.git
cd PenerapanDataSainsProyekPertama
python -m venv env
venv\Scripts\activate
pip install -r requirements.txt

```

## Conclusion

Proyek ini bertujuan untuk membantu departemen Human Resources (HR) di perusahaan Jaya Jaya Maju dalam memahami dan mengatasi tingginya angka attrition (karyawan keluar). Melalui analisis data dan visualisasi interaktif dalam bentuk business dashboard, beberapa insight penting berhasil diperoleh:

- **Jumlah yang resign:** 179 karyawan
- **Gender:** Laki-laki sedikit lebih dominan melakukan resign dibanding perempuan
- **Rata-rata umur:** 33,47 tahun (usia produktif)
- **Rata-rata masa kerja:** 5,19 tahun (menunjukkan potensi stagnasi karir)
- **Rata-rata pendapatan bulanan:** 4.873
- **Jumlah yang resign:** 179 karyawan
- **Gender:** Laki-laki sedikit lebih dominan melakukan resign dibanding perempuan
- **Rata-rata umur:** 33,47 tahun (usia produktif)
- **Rata-rata masa kerja:** 5,19 tahun (menunjukkan potensi stagnasi karir)
- **Rata-rata pendapatan bulanan:** Rp4.873.000
- **Bidang pendidikan dominan:** Life Sciences dan Medical
- **Job role dengan gaji lebih rendah** cenderung memiliki tingkat attrition lebih tinggi dibandingkan role seperti Manager dan Research Director

- **Bidang pendidikan dominan:** Life Sciences dan Medical
- **Job role dengan gaji lebih rendah** cenderung memiliki tingkat attrition lebih tinggi dibandingkan role seperti Manager dan Research Director

Dengan adanya dashboard ini, departemen HR dapat **mengambil keputusan berbasis data** secara lebih cepat dan tepat, misalnya dalam menyusun strategi retensi karyawan, perencanaan rekrutmen, serta pengembangan kebijakan kesejahteraan karyawan yang lebih baik.

Proyek ini membuktikan bahwa pendekatan data science dan visualisasi dapat memberikan nilai tambah nyata bagi pengambilan keputusan di bidang sumber daya manusia.


### Rekomendasi Action Items

Berdasarkan temuan dari analisis data dan insight yang diperoleh melalui dashboard, berikut adalah beberapa rekomendasi action items yang dapat dilakukan oleh perusahaan Jaya Jaya Maju untuk menurunkan tingkat attrition dan meningkatkan retensi karyawan:

- **Melakukan employee engagement survey secara rutin**  
  Guna mengetahui kepuasan, motivasi, dan aspirasi karyawan agar perusahaan dapat merespons kebutuhan mereka secara proaktif.

- **Meningkatkan program pelatihan dan pengembangan karier**  
  Khususnya untuk karyawan di bidang atau peran yang memiliki tingkat attrition tinggi, seperti Sales dan Research, untuk meningkatkan loyalitas dan keinginan bertahan.

- **Meninjau ulang struktur kompensasi dan benefit**  
  Melakukan benchmarking terhadap rata-rata pendapatan dan memastikan fairness antar posisi dan divisi agar karyawan merasa dihargai.

- **Mengembangkan program retensi untuk kelompok rentan**  
  Misalnya karyawan dengan masa kerja di bawah 3 tahun atau di usia produktif yang cenderung lebih mobile, dengan pendekatan personalisasi atau insentif tambahan.

- **Mengoptimalkan penggunaan dashboard secara berkala**  
  Agar manajer HR dapat terus memantau indikator kunci dan segera mengambil tindakan jika ada tren negatif yang muncul.


