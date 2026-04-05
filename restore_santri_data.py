#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmk.settings')
django.setup()

from administrator.models import Cabang, Tingkat, Kelas, Santri

def restore_santri_data():
    """Restore previous Santri data"""
    
    print("Restoring Santri data...")
    
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
    
    # Restore Santri data
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
            print(f"+ Restored santri: {santri.nama} ({santri.nis})")
        else:
            print(f"= Santri already exists: {santri.nama} ({santri.nis})")
    
    print(f"\n+ Santri data restored successfully!")
    print(f"Summary:")
    print(f"   - Cabang: {Cabang.objects.count()}")
    print(f"   - Tingkat: {Tingkat.objects.count()}")
    print(f"   - Kelas: {Kelas.objects.count()}")
    print(f"   - Santri: {Santri.objects.count()}")
    
    # Display all Santri
    print(f"\nAll Santri Records:")
    for santri in Santri.objects.all():
        print(f"   - {santri.nis}: {santri.nama} (Kelas: {santri.kelas.nama_kelas})")

if __name__ == '__main__':
    restore_santri_data()
