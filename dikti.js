const axios = require('axios');

async function cariDataMahasiswa(data) {
    try {
        const response = await axios.get(`https://pddikti.kemdikbud.go.id/api/pencarian/mhs/${data}`);
        const detailResponse = await axios.get(`https://pddikti.kemdikbud.go.id/api/detail/mhs/${response.data[0].id}`);
        
        const mhsData = detailResponse.data;
        
        console.log('\nData ditemukan!');
        console.log(`[+] NIM                     : ${mhsData.nim}`);
        console.log(`[+] Nama                    : ${mhsData.nama}`);
        console.log(`[+] Perguruan tinggi        : ${mhsData.nama_pt}`);
        console.log(`[+] Jenis kelamin           : ${mhsData.jenis_kelamin}`);
        console.log(`[+] Tahun masuk             : ${mhsData.tahun_masuk}`);
        console.log(`[+] Jenjang - prodi         : ${mhsData.jenjang} - ${mhsData.prodi}`);
        console.log(`[+] Status awal mahasiswa   : ${mhsData.jenis_daftar}`);
        console.log(`[+] Status akhir mahasiswa  : ${mhsData.status_saat_ini}`);
    
    } catch (err) {
        console.log(`Terjadi kesalahan: ${err}`);
    }
}

// Input manual dari pengguna
(async () => {
    while (true) {
        const nimMahasiswa = prompt("\nMasukkan NIM atau nama mahasiswa dan nama perguruan tinggi (atau 'q' untuk keluar): ");
        if (nimMahasiswa.toLowerCase() === 'q') {
            console.log("Terima kasih telah menggunakan layanan ini.");
            break;
        }
        await cariDataMahasiswa(nimMahasiswa);
    }
})();
