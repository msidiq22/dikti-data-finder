import requests
import csv
import time

def cari_data_mahasiswa(data):
    try:
        dikti = requests.get(f'https://pddikti.kemdikbud.go.id/api/pencarian/mhs/{data}')
        dikti.raise_for_status()
        
        # Memastikan ada hasil pencarian
        results = dikti.json()
        if results:
            all_mhs_data = []
            for result in results:
                detail_mhs = requests.get(f'https://pddikti.kemdikbud.go.id/api/detail/mhs/{result["id"]}')
                detail_mhs.raise_for_status()
                
                mhs_data = detail_mhs.json()
                all_mhs_data.append({
                    "nim": mhs_data["nim"],
                    "nama": mhs_data["nama"],
                    "nama_pt": mhs_data["nama_pt"],
                    "jenis_kelamin": mhs_data["jenis_kelamin"],
                    "tahun_masuk": mhs_data["tahun_masuk"],
                    "jenjang": mhs_data["jenjang"],
                    "prodi": mhs_data["prodi"],
                    "jenis_daftar": mhs_data["jenis_daftar"],
                    "status_saat_ini": mhs_data["status_saat_ini"]
                })
            return all_mhs_data
        else:
            print(f'Tidak ada data ditemukan untuk: {data}')
            return []

    except requests.RequestException as err:
        print(f'Terjadi kesalahan: {err}')
        return []

# Input dari file dan output ke file CSV
def main():
    input_file = 'daftar.txt'  # Ganti dengan nama file Anda
    output_file = 'data_mahasiswa.csv'
    
    with open(input_file, 'r') as f:
        mahasiswa_list = f.read().splitlines()

    total_mahasiswa = len(mahasiswa_list)

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ["nim", "nama", "nama_pt", "jenis_kelamin", "tahun_masuk", "jenjang", "prodi", "jenis_daftar", "status_saat_ini"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for idx, mahasiswa in enumerate(mahasiswa_list, start=1):
            print(f'Memproses {idx}/{total_mahasiswa}: {mahasiswa}')
            mhs_data_list = cari_data_mahasiswa(mahasiswa)
            if mhs_data_list:
                for mhs_data in mhs_data_list:
                    writer.writerow(mhs_data)
                    print(f'Data untuk {mhs_data["nim"]} ({mhs_data["nama"]}) berhasil ditambahkan ke CSV.')
            else:
                print(f'Tidak ada data untuk {mahasiswa}.')
            
            # Menambahkan delay 2 detik
            time.sleep(2)

            # Menampilkan progres
            progress = (idx / total_mahasiswa) * 100
            print(f'Progres: {progress:.2f}%')

    print(f'Semua data telah diproses dan disimpan ke {output_file}.')

if __name__ == '__main__':
    main()
