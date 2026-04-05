#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmk.settings')
django.setup()

from administrator.models import *

def check_existing_data():
    """Check all existing data in database"""
    
    print("=== CHECKING EXISTING DATA ===\n")
    
    # Check Santri
    print("=== SANTRI ===")
    santri_list = Santri.objects.all()
    if santri_list:
        for s in santri_list:
            kelas_name = s.kelas.nama_kelas if s.kelas else "No Class"
            print(f'{s.nis}: {s.nama} - {kelas_name}')
        print(f"Total Santri: {santri_list.count()}")
    else:
        print("No Santri data found")
    
    # Check Kelas
    print("\n=== KELAS ===")
    kelas_list = Kelas.objects.all()
    if kelas_list:
        for k in kelas_list:
            tingkat_name = k.tingkat.nama_tingkat if k.tingkat else "No Tingkat"
            cabang_name = k.cabang.nama_cabang if k.cabang else "No Cabang"
            print(f'{k.nama_kelas} - {tingkat_name} - {cabang_name}')
        print(f"Total Kelas: {kelas_list.count()}")
    else:
        print("No Kelas data found")
    
    # Check Guru
    print("\n=== GURU ===")
    guru_list = Guru.objects.all()
    if guru_list:
        for g in guru_list:
            print(f'{g.nama_guru}')
        print(f"Total Guru: {guru_list.count()}")
    else:
        print("No Guru data found")
    
    # Check Jadwal
    print("\n=== JADWAL ===")
    jadwal_list = Jadwal.objects.all()
    if jadwal_list:
        for j in jadwal_list:
            mapel_name = j.mata_pelajaran.nama_mapel if j.mata_pelajaran else "No Mapel"
            kelas_name = j.kelas.nama_kelas if j.kelas else "No Kelas"
            guru_name = j.guru.nama_guru if j.guru else "No Guru"
            print(f'{j.hari} {j.jam_mulai}-{j.jam_selesai} - {mapel_name} - {kelas_name} - {guru_name}')
        print(f"Total Jadwal: {jadwal_list.count()}")
    else:
        print("No Jadwal data found")
    
    # Check Mata Pelajaran
    print("\n=== MATA PELAJARAN ===")
    mapel_list = MataPelajaran.objects.all()
    if mapel_list:
        for m in mapel_list:
            print(f'{m.nama_mapel}')
        print(f"Total Mata Pelajaran: {mapel_list.count()}")
    else:
        print("No Mata Pelajaran data found")
    
    # Check Cabang
    print("\n=== CABANG ===")
    cabang_list = Cabang.objects.all()
    if cabang_list:
        for c in cabang_list:
            print(f'{c.nama_cabang}')
        print(f"Total Cabang: {cabang_list.count()}")
    else:
        print("No Cabang data found")
    
    # Check Tingkat
    print("\n=== TINGKAT ===")
    tingkat_list = Tingkat.objects.all()
    if tingkat_list:
        for t in tingkat_list:
            print(f'{t.nama_tingkat}')
        print(f"Total Tingkat: {tingkat_list.count()}")
    else:
        print("No Tingkat data found")

if __name__ == '__main__':
    check_existing_data()
