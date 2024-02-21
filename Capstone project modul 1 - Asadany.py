from tabulate import tabulate

data_karyawan = {
    "Gon": "1234567",
    "Komeng": "abcdefg",
    "Zara": "123abc"
}

data = [
    {"id": "1", "Nama": "Anang", "Umur": "22", "Poli": "Umum", "Status": "Outpatient"},
    {"id": "2", "Nama": "Buni", "Umur": "34", "Poli": "kandungan", "Status": "Inpatient"},
    {"id": "3", "Nama": "Mail", "Umur": "25", "Poli": "Mata", "Status": "Outpatient"},
    {"id": "4", "Nama": "Nana", "Umur": "37", "Poli": "Gigi", "Status": "Outpatient"},
    {"id": "5", "Nama": "Ujang", "Umur": "41", "Poli": "Umum", "Status": "Outpatient"}
]

def read_data():
    print(tabulate(data, headers='keys', tablefmt='pretty'))

def create_data():
    print("Silahkan tambahkan data pasien")
    while True:
        namaBaru = input('Masukkan Nama pasien: ')
        if namaBaru.isalpha():
            break
        else:
            print("Nama Pasien hanya boleh berisi huruf, silahkan coba lagi")
    umurBaru = get_input('Masukkan umur pasien: ', int)
    poliBaru = input('Masukkan poli pasien: ')
    while True:
        statusBaru = input('Masukkan status pasien (Inpatient/ Outpatient): ')
        if statusBaru in ["Inpatient", "Outpatient"]:
            break
        else:
            print("Status pasien tidak valid, mohon isi Inpatient atau Outpatient")
    idBaru = len(data) + 1

    new_data = {"id": idBaru, "Nama": namaBaru, "Umur": umurBaru, "Poli": poliBaru, "Status": statusBaru}
    data.append(new_data)

    print("Data Pasien Berhasil Ditambah!!!")

def Sort_data():
    data_sort = input("Masukan Data yang ingin anda Sort (ID /Nama/ Umur/ Poli/ Status):").lower()

    if data_sort in ['id', 'nama', 'umur', 'poli', 'status']:
        if data_sort == 'Umur':
            sorted_data = sorted(data, key=lambda x: int(x[data_sort]))
        else:
            sorted_data = sorted(data, key=lambda x: x[data_sort.capitalize()])
        print(tabulate(sorted_data, headers='keys', tablefmt='pretty'))
    else:
        print("Data yang Anda masukkan tidak valid")

def update_data():
    print("Silahkan update data pasien")
    Nama_update = input('Masukkan Nama pasien yang ingin diupdate: ')
    Pasien_update = next((pasien for pasien in data if pasien['Nama'].lower() == Nama_update.lower()), None)
    if Pasien_update:
        print("Data pasien yang ingin diupdate:")
        print(tabulate([Pasien_update], headers='keys', tablefmt='pretty'))
        kolom = input('Masukkan data yang ingin diupdate (Nama, Umur, Poli, Status): ')
        if kolom == 'Umur':
            Pasien_update['Umur'] = get_input(f"Masukkan {kolom} baru : ", int)
        elif kolom == 'Nama':
            while True:
                new_name = input("Masukkan Nama baru: ")
                if new_name.isalpha():
                    Pasien_update['Nama'] = new_name
                    break
        elif kolom == 'Status':
            while True:
                new_status = input('Masukkan status pasien (Inpatient/ Outpatient): ')
                if new_status in ["Inpatient", "Outpatient"]:
                    Pasien_update['Status'] = new_status
                    break
                else:
                    print("Status pasien tidak valid, mohon isi Inpatient atau Outpatient")
        else:
            value = input(f"Masukkan update {kolom} baru : ")
            Pasien_update[kolom] = value
        print("Data Pasien Berhasil Diupdate!!!")
    else:
        print("Nama pasien tidak ditemukan.")

def delete_data():
    print("Silahkan hapus data pasien")
    nama_delete = input('Masukkan Nama pasien yang ingin dihapus: ')
    global data
    data = [pasien for pasien in data if pasien['Nama'].lower() != nama_delete.lower()]
    print("Data Pasien Berhasil Dihapus!!!")

def search_data(attribute, value):
    results = [pasien for pasien in data if pasien.get(attribute) == value]
    return results

def Summary_data():
    total_patients = len(data)
    if total_patients == 0:
        print("No patient data available.")
        return

    
    total_age = sum(int(patient['Umur']) for patient in data)
    average_age = total_age / total_patients

   
    status_counts = {'Inpatient': 0, 'Outpatient': 0}
    for patient in data:
        status_counts[patient['Status']] += 1

    
    poli_counts = {}
    for patient in data:
        poli = patient['Poli']
        poli_counts[poli] = poli_counts.get(poli, 0) + 1
    most_common_poli = max(poli_counts, key=poli_counts.get)

   
    summary_data = [
        ["Total Pasien", total_patients],
        ["Umur Rata - Rata Pasien", f"{average_age:.2f} years"],
        ["Jumlah Inpatients", status_counts['Inpatient']],
        ["Jumlah Outpatients", status_counts['Outpatient']],
        ["Poli Dengan Jumlah Pasien terbanyak", f"{most_common_poli} ({poli_counts[most_common_poli]} patients)"]
    ]

    
    print("Summary of Patient Data:")
    print(tabulate(summary_data, headers=["Item", "Keterangan"], tablefmt='grid'))


def get_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Input yang dimasukkan tidak valid. Silakan coba lagi.")

def login():
    while True:
        print('''
        🏥Selamat Datang di RS Sumber Sehat Jaya🏥
        ''')
        ID = input("Masukkan ID Anda: ")
        Password = input("Masukkan password: ")
        if ID in data_karyawan and data_karyawan[ID] == Password:
            print("Login berhasil!")
            break
        else:
            print("ID atau Password salah. Silakan coba lagi.")

def main():
    login()

    while True:
        print('''
        ####### DATABASE PASIEN ######
              RS SUMBER SEHAT JAYA

        Menu Utama
        1. Lihat Data Pasien
        2. Tambah Data Pasien
        3. Update Data Pasien
        4. Hapus Data Pasien
        5. Cari Data Pasien
        6. Sortir Data Pasien
        7. Summary Data Pasien
        8. Keluar
        ''')

        opsi = input("Pilih menu:")
        if opsi == '1':
            read_data()
        elif opsi == '2':
            create_data()
        elif opsi == '3':
            update_data()
        elif opsi == '4':
            delete_data()
        elif opsi == '5':
            valid_attributes = ['Nama', 'Umur', 'Poli', 'Status']
            attribute = input("Mohon pilih data yang ingin Anda cari (Nama, Umur, Poli, Status): ").capitalize()
            if attribute not in valid_attributes:
                print("Data tidak ditemukan. Mohon masukkan data (Nama, Umur, Poli, Status).")
            else:
                value = input(f"Masukkan {attribute} yang Anda cari : ")
                search_results = search_data(attribute, value)
                if search_results:
                    print(tabulate(search_results, headers='keys', tablefmt='pretty'))
                else:
                    print("Data tidak ditemukan.")
        elif opsi == '6':
            Sort_data()
        elif opsi =='7':
            Summary_data()
        elif opsi == '8':
            break
        else:
            print("Input Anda tidak valid!")

main()