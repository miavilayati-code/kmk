#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmk.settings')
django.setup()

from administrator.models import Cabang, Tingkat, Kelas, Santri, TahunAkademik, Semester, MataPelajaran, Guru, Jadwal
from django.contrib.auth.models import User

def create_sample_data():
    """Create sample data for testing"""
    
    print("Creating sample data...")
    
    # Create Cabang
    cabang, created = Cabang.objects.get_or_create(
        nama_cabang="KMK Pusat"
    )
    if created:
        print(f"+ Created cabang: {cabang.nama_cabang}")
    
    # Create Tingkat
    tingkat_data = [
        {"nama_tingkat": "Ibtidaiyah 1"},
        {"nama_tingkat": "Ibtidaiyah 2"},
        {"nama_tingkat": "Ibtidaiyah 3"},
        {"nama_tingkat": "Ibtidaiyah 4"},
        {"nama_tingkat": "Ibtidaiyah 5"},
        {"nama_tingkat": "Ibtidaiyah 6"},
    ]
    
    for data in tingkat_data:
        tingkat, created = Tingkat.objects.get_or_create(**data)
        if created:
            print(f"+ Created tingkat: {tingkat.nama_tingkat}")
    
    # Create Tahun Akademik
    tahun_akademik, created = TahunAkademik.objects.get_or_create(
        tahun="2025/2026",
        aktif=True
    )
    if created:
        print(f"+ Created tahun akademik: {tahun_akademik.tahun}")
    
    # Create Semester
    semester_data = [
        {"nama_semester": "Ganjil", "tahun_akademik": tahun_akademik},
        {"nama_semester": "Genap", "tahun_akademik": tahun_akademik},
    ]
    
    for data in semester_data:
        semester, created = Semester.objects.get_or_create(**data)
        if created:
            print(f"+ Created semester: {semester.nama_semester} {semester.tahun_akademik}")
    
    # Create Kelas
    kelas_data = [
        {"nama_kelas": "1A", "tingkat": Tingkat.objects.get(nama_tingkat="Ibtidaiyah 1"), "cabang": cabang},
        {"nama_kelas": "1B", "tingkat": Tingkat.objects.get(nama_tingkat="Ibtidaiyah 1"), "cabang": cabang},
        {"nama_kelas": "2A", "tingkat": Tingkat.objects.get(nama_tingkat="Ibtidaiyah 2"), "cabang": cabang},
        {"nama_kelas": "2B", "tingkat": Tingkat.objects.get(nama_tingkat="Ibtidaiyah 2"), "cabang": cabang},
    ]
    
    for data in kelas_data:
        kelas, created = Kelas.objects.get_or_create(**data)
        if created:
            print(f"+ Created kelas: {kelas.nama_kelas}")
    
    # Create Mata Pelajaran
    mapel_data = [
        {"nama_mapel": "Al-Qur'an Hadits"},
        {"nama_mapel": "Akidah"},
        {"nama_mapel": "Fiqih"},
        {"nama_mapel": "Tauhid"},
        {"nama_mapel": "Bahasa Arab"},
        {"nama_mapel": "Bahasa Indonesia"},
        {"nama_mapel": "Matematika"},
        {"nama_mapel": "IPA"},
        {"nama_mapel": "IPS"},
    ]
    
    for data in mapel_data:
        mapel, created = MataPelajaran.objects.get_or_create(**data)
        if created:
            print(f"+ Created mata pelajaran: {mapel.nama_mapel}")
    
    # Create Guru
    guru_data = [
        {"nama_guru": "Ustadz Ahmad Rohman"},
        {"nama_guru": "Ustadzah Fatimah Azzahra"},
        {"nama_guru": "Ustadz Muhammad Yusuf"},
    ]
    
    for data in guru_data:
        guru, created = Guru.objects.get_or_create(**data)
        if created:
            print(f"+ Created guru: {guru.nama_guru}")
    
    # Create Santri
    kelas_1a = Kelas.objects.get(nama_kelas="1A")
    santri_data = [
        {"nama": "Ahmad Rizki", "nis": "2025001", "kelas": kelas_1a},
        {"nama": "Siti Nurhaliza", "nis": "2025002", "kelas": kelas_1a},
        {"nama": "Muhammad Fadli", "nis": "2025003", "kelas": kelas_1a},
        {"nama": "Aisyah Putri", "nis": "2025004", "kelas": kelas_1a},
        {"nama": "Budi Santoso", "nis": "2025005", "kelas": kelas_1a},
    ]
    
    for data in santri_data:
        santri, created = Santri.objects.get_or_create(**data)
        if created:
            print(f"+ Created santri: {santri.nama} ({santri.nis})")
    
    # Create Jadwal
    semester_ganjil = Semester.objects.get(nama_semester="Ganjil")
    jadwal_data = [
        {
            "hari": "Senin",
            "jam_mulai": "07:00:00",
            "jam_selesai": "08:30:00",
            "mata_pelajaran": MataPelajaran.objects.get(nama_mapel="Al-Qur'an Hadits"),
            "guru": Guru.objects.get(nama_guru="Ustadz Ahmad Rohman"),
            "kelas": kelas_1a,
            "semester": semester_ganjil
        },
        {
            "hari": "Senin",
            "jam_mulai": "08:30:00",
            "jam_selesai": "10:00:00",
            "mata_pelajaran": MataPelajaran.objects.get(nama_mapel="Akidah"),
            "guru": Guru.objects.get(nama_guru="Ustadzah Fatimah Azzahra"),
            "kelas": kelas_1a,
            "semester": semester_ganjil
        },
        {
            "hari": "Selasa",
            "jam_mulai": "07:00:00",
            "jam_selesai": "08:30:00",
            "mata_pelajaran": MataPelajaran.objects.get(nama_mapel="Fiqih"),
            "guru": Guru.objects.get(nama_guru="Ustadz Muhammad Yusuf"),
            "kelas": kelas_1a,
            "semester": semester_ganjil
        },
    ]
    
    for data in jadwal_data:
        jadwal, created = Jadwal.objects.get_or_create(**data)
        if created:
            print(f"+ Created jadwal: {jadwal.hari} {jadwal.mata_pelajaran.nama_mapel}")
    
    print("\n+ Sample data created successfully!")
    print(f"Summary:")
    print(f"   - Cabang: {Cabang.objects.count()}")
    print(f"   - Tingkat: {Tingkat.objects.count()}")
    print(f"   - Kelas: {Kelas.objects.count()}")
    print(f"   - Mata Pelajaran: {MataPelajaran.objects.count()}")
    print(f"   - Guru: {Guru.objects.count()}")
    print(f"   - Santri: {Santri.objects.count()}")
    print(f"   - Jadwal: {Jadwal.objects.count()}")

if __name__ == '__main__':
    create_sample_data()
