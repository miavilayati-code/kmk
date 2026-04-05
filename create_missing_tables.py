#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmk.settings')
django.setup()

from django.db import connection

def create_missing_tables():
    """Create missing tables manually"""
    
    print("Creating missing tables...")
    
    cursor = connection.cursor()
    
    # Create Jadwal table
    create_jadwal_sql = """
    CREATE TABLE IF NOT EXISTS administrator_jadwal (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        hari VARCHAR(10) NOT NULL,
        jam_mulai TIME NOT NULL,
        jam_selesai TIME NOT NULL,
        mata_pelajaran_id BIGINT NOT NULL,
        guru_id BIGINT NOT NULL,
        kelas_id BIGINT NOT NULL,
        semester_id BIGINT NOT NULL,
        FOREIGN KEY (mata_pelajaran_id) REFERENCES administrator_matapelajaran(id),
        FOREIGN KEY (guru_id) REFERENCES administrator_guru(id),
        FOREIGN KEY (kelas_id) REFERENCES administrator_kelas(id),
        FOREIGN KEY (semester_id) REFERENCES administrator_semester(id)
    )
    """
    
    # Create Absensi table
    create_absensi_sql = """
    CREATE TABLE IF NOT EXISTS administrator_absensi (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        santri_id BIGINT NOT NULL,
        jadwal_id BIGINT NOT NULL,
        tanggal DATE NOT NULL,
        status VARCHAR(20) NOT NULL,
        FOREIGN KEY (santri_id) REFERENCES administrator_santri(id),
        FOREIGN KEY (jadwal_id) REFERENCES administrator_jadwal(id)
    )
    """
    
    # Create Nilai table
    create_nilai_sql = """
    CREATE TABLE IF NOT EXISTS administrator_nilai (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        santri_id BIGINT NOT NULL,
        mata_pelajaran_id BIGINT NOT NULL,
        semester_id BIGINT NOT NULL,
        nilai INT NOT NULL,
        FOREIGN KEY (santri_id) REFERENCES administrator_santri(id),
        FOREIGN KEY (mata_pelajaran_id) REFERENCES administrator_matapelajaran(id),
        FOREIGN KEY (semester_id) REFERENCES administrator_semester(id)
    )
    """
    
    try:
        print("Creating Jadwal table...")
        cursor.execute(create_jadwal_sql)
        print("+ Jadwal table created")
        
        print("Creating Absensi table...")
        cursor.execute(create_absensi_sql)
        print("+ Absensi table created")
        
        print("Creating Nilai table...")
        cursor.execute(create_nilai_sql)
        print("+ Nilai table created")
        
        connection.commit()
        print("\n+ All missing tables created successfully!")
        
    except Exception as e:
        print(f"\n- Error creating tables: {e}")
        connection.rollback()
    finally:
        cursor.close()
    
    # Check tables
    print("\n=== CHECKING TABLES ===")
    cursor = connection.cursor()
    cursor.execute('SHOW TABLES')
    tables = [table[0] for table in cursor.fetchall() if 'administrator' in table[0]]
    for table in sorted(tables):
        print(f"+ {table}")
    cursor.close()

if __name__ == '__main__':
    create_missing_tables()
