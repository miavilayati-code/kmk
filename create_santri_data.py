#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmk.settings')
django.setup()

from administrator.models import Cabang, Tingkat, Kelas, Santri, TahunAkademik, Semester, MataPelajaran, Guru, Jadwal
from django.contrib.auth.models import User

def create_santri_data():
    """Create Santri data only"""
    
    print("Creating Santri data...")
    
    # Create Cabang if not exists
    cabang, created = Cabang.objects.get_or_create(
        nama_cabang="KMK Pusat"
    )
    if created:
        print(f"+ Created cabang: {cabang.nama_cabang}")
    
    # Create Tingkat if not exists
    tingkat, created = Tingkat.objects.get_or_create(
        nama_tingkat="Ibtidaiyah 1"
    )
    if created:
        print(f"+ Created tingkat: {tingkat.nama_tingkat}")
    
    # Create Kelas if not exists
    kelas, created = Kelas.objects.get_or_create(
        nama_kelas="1A",
        tingkat=tingkat,
        cabang=cabang
    )
    if created:
        print(f"+ Created kelas: {kelas.nama_kelas}")
    
    # Create Santri data
    santri_data = [
        {"nama": "Ahmad Rizki", "nis": "2025001", "kelas": kelas},
        {"nama": "Siti Nurhaliza", "nis": "2025002", "kelas": kelas},
        {"nama": "Muhammad Fadli", "nis": "2025003", "kelas": kelas},
        {"nama": "Aisyah Putri", "nis": "2025004", "kelas": kelas},
        {"nama": "Budi Santoso", "nis": "2025005", "kelas": kelas},
    ]
    
    for data in santri_data:
        santri, created = Santri.objects.get_or_create(**data)
        if created:
            print(f"+ Created santri: {santri.nama} ({santri.nis})")
    
    print(f"\n+ Santri data created successfully!")
    print(f"Summary:")
    print(f"   - Cabang: {Cabang.objects.count()}")
    print(f"   - Tingkat: {Tingkat.objects.count()}")
    print(f"   - Kelas: {Kelas.objects.count()}")
    print(f"   - Santri: {Santri.objects.count()}")

if __name__ == '__main__':
    create_santri_data()
