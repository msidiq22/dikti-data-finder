# DIKTI Data Finder

**DIKTI Data Finder** adalah alat pencari data mahasiswa berbasis API DIKTI yang mendukung dua bahasa pemrograman, yaitu **JavaScript** dan **Python**. Dengan alat ini, Anda dapat melakukan pencarian data mahasiswa dengan cepat dan mudah melalui berbagai platform, termasuk **Windows**, **macOS**, **Linux**, dan **Android** melalui aplikasi **Termux**.

## Tentang DIKTI
**DIKTI** (Direktorat Jenderal Pendidikan Tinggi) adalah lembaga yang mengelola pendidikan tinggi di Indonesia di bawah Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi. DIKTI juga menyediakan akses ke data perguruan tinggi dan mahasiswa.

## Fitur
- Pencarian data mahasiswa menggunakan API DIKTI
- Mendukung bahasa pemrograman **JavaScript** dan **Python**
- Kompatibel dengan **Windows**, **macOS**, **Linux**, dan **Android** (Termux)
- Memungkinkan integrasi mudah dengan proyek lain melalui API

## Bahasa Pemrograman dan Modul Yang Dipakai
- **JavaScript**: Axios digunakan untuk melakukan permintaan HTTP
- **Python**: Requests module digunakan untuk melakukan permintaan HTTP

## Instalasi

### 1. Instalasi di Windows, macOS, atau Linux
**JavaScript (Node.js)**
1. Pastikan [Node.js](https://nodejs.org/) telah diinstal.
2. Instal **Axios (Sudah include di file package.json)**:
   ```bash
   npm install
   ```
3. Instal **Git** jika belum terpasang:
   - Windows: [Download Git](https://git-scm.com/download/win)
   - macOS/Linux:
     ```bash
     sudo apt-get install git
     ```
4. Clone repositori proyek ini:
   ```bash
   git clone https://github.com/maulananais/dikti-data-finder.git
   ```
5. Masuk ke direktori proyek:
   ```bash
   cd dikti-data-finder
   ```
6. Jalankan skrip dengan perintah:
   ```bash
   node dikti.js
   ```

**Python**
1. Pastikan [Python](https://www.python.org/) dan [pip](https://pip.pypa.io/en/stable/installation/) sudah terinstal.
2. Instal modul **Requests**:
   ```bash
   pip install requests
   ```
3. Clone repositori proyek ini:
   ```bash
   git clone https://github.com/maulananais/dikti-data-finder.git
   ```
4. Masuk ke direktori proyek:
   ```bash
   cd dikti-data-finder
   ```
5. Jalankan skrip Python sesuai dengan perangkat Anda:
   - Windows:
     ```bash
     python dikti.py
     ```
   - macOS/Linux:
     ```bash
     python3 dikti.py
     ```

### 2. Instalasi di Termux (Android)
**Langkah Instalasi di Termux:**
1. Instal aplikasi **Termux** dari Play Store atau F-Droid.
2. Buka Termux dan jalankan perintah berikut untuk menginstal **Node.js**, **Python**, dan **Git**:
   ```bash
   pkg update
   pkg install nodejs python git
   ```
3. Clone repositori proyek ini dengan perintah:
   ```bash
   git clone https://github.com/maulananais/dikti-data-finder.git
   ```
4. Masuk ke direktori proyek:
   ```bash
   cd dikti-data-finder
   ```

**JavaScript (Node.js)**
1. Instal **Axios**:
   ```bash
   npm install axios
   ```
2. Jalankan skrip dengan:
   ```bash
   node dikti.js
   ```

**Python**
1. Instal modul **Requests**:
   ```bash
   pip install requests
   ```
2. Jalankan skrip dengan:
   ```bash
   python dikti.py
   ```

### Donasi

Jika Anda ingin mendukung pengembangan proyek ini, silakan berdonasi melalui [Saweria](https://saweria.co/maulananais).

---

### Terima Kasih Kepada:
- Allah SWT
- Orang tua saya
- Pacar saya
- [PDDIKTI](https://pddikti.kemdikbud.go.id) untuk data dan sumber dayanya
- [Node.js](https://nodejs.org) untuk platform backend
- [Git](https://git-scm.com) untuk version control

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT.
