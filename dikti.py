import requests

def cari_data_mahasiswa(data):
    try:
        dikti = requests.get(f'https://pddikti.kemdikbud.go.id/api/pencarian/mhs/{data}')
        dikti.raise_for_status()
        detail_mhs = requests.get(f'https://pddikti.kemdikbud.go.id/api/detail/mhs/{dikti.json()[0]["id"]}')
        detail_mhs.raise_for_status()
        
        mhs_data = detail_mhs.json()
        
        print('\nData ditemukan!')
        print(f'[+] NIM                     : {mhs_data["nim"]}')
        print(f'[+] Nama                    : {mhs_data["nama"]}')
        print(f'[+] Perguruan tinggi        : {mhs_data["nama_pt"]}')
        print(f'[+] Jenis kelamin           : {mhs_data["jenis_kelamin"]}')
        print(f'[+] Tahun masuk             : {mhs_data["tahun_masuk"]}')
        print(f'[+] Jenjang - prodi         : {mhs_data["jenjang"]} - {mhs_data["prodi"]}')
        print(f'[+] Status awal mahasiswa   : {mhs_data["jenis_daftar"]}')
        print(f'[+] Status akhir mahasiswa  : {mhs_data["status_saat_ini"]}')
    
    except requests.RequestException as err:
        print(f'Terjadi kesalahan: {err}')

# Input manual dari pengguna
while True:
    nim_mahasiswa = input("\nMasukkan NIM atau nama mahasiswa dan nama perguruan tinggi (atau 'q' untuk keluar): ")
    if nim_mahasiswa.lower() == 'q':
        print("Terima kasih telah menggunakan layanan ini.")
        break
    cari_data_mahasiswa(nim_mahasiswa)
