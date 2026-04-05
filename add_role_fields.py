#!/usr/bin/env python
import os
import django
import pymysql

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmk.settings')
django.setup()

# Database connection parameters
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'absensi_santri'

def add_role_fields():
    """Add role-related fields to auth_user table"""
    
    try:
        # Connect to MySQL server
        connection = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        
        cursor = connection.cursor()
        
        print("Adding role fields to auth_user table...")
        
        # Add role field
        try:
            cursor.execute("""
                ALTER TABLE auth_user 
                ADD COLUMN role VARCHAR(20) DEFAULT 'muallimat' COMMENT 'User role'
            """)
            print("+ Added role field")
        except pymysql.Error as e:
            if "Duplicate column name" in str(e):
                print("+ Role field already exists")
            else:
                print(f"- Error adding role field: {e}")
        
        # Add nip field
        try:
            cursor.execute("""
                ALTER TABLE auth_user 
                ADD COLUMN nip VARCHAR(20) UNIQUE NULL COMMENT 'NIP'
            """)
            print("+ Added nip field")
        except pymysql.Error as e:
            if "Duplicate column name" in str(e):
                print("+ NIP field already exists")
            else:
                print(f"- Error adding nip field: {e}")
        
        # Add phone field
        try:
            cursor.execute("""
                ALTER TABLE auth_user 
                ADD COLUMN phone VARCHAR(15) NULL COMMENT 'Phone number'
            """)
            print("+ Added phone field")
        except pymysql.Error as e:
            if "Duplicate column name" in str(e):
                print("+ Phone field already exists")
            else:
                print(f"- Error adding phone field: {e}")
        
        # Add photo field
        try:
            cursor.execute("""
                ALTER TABLE auth_user 
                ADD COLUMN photo VARCHAR(255) NULL COMMENT 'Profile photo'
            """)
            print("+ Added photo field")
        except pymysql.Error as e:
            if "Duplicate column name" in str(e):
                print("+ Photo field already exists")
            else:
                print(f"- Error adding photo field: {e}")
        
        # Add created_at field
        try:
            cursor.execute("""
                ALTER TABLE auth_user 
                ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Created at'
            """)
            print("+ Added created_at field")
        except pymysql.Error as e:
            if "Duplicate column name" in str(e):
                print("+ Created_at field already exists")
            else:
                print(f"- Error adding created_at field: {e}")
        
        # Add updated_at field
        try:
            cursor.execute("""
                ALTER TABLE auth_user 
                ADD COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Updated at'
            """)
            print("+ Added updated_at field")
        except pymysql.Error as e:
            if "Duplicate column name" in str(e):
                print("+ Updated_at field already exists")
            else:
                print(f"- Error adding updated_at field: {e}")
        
        connection.commit()
        cursor.close()
        connection.close()
        
        print("\n+ All role fields have been added successfully!")
        
    except pymysql.Error as e:
        print(f"- Database error: {e}")
    except Exception as e:
        print(f"- Unexpected error: {e}")

if __name__ == '__main__':
    add_role_fields()
