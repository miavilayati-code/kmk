#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmk.settings')
django.setup()

from django.contrib.auth import get_user_model
from administrator.models import User

def create_role_users():
    """Create users with different roles"""
    
    users_data = [
        {
            'username': 'admin_madin',
            'email': 'admin.madin@kmk.sch.id',
            'first_name': 'Admin',
            'last_name': 'Madin',
            'password': 'admin123',
            'role': 'admin_madin',
            'is_staff': True,
            'is_superuser': True,
            'nip': 'ADM001',
            'phone': '08123456789'
        },
        {
            'username': 'koordinator_kmk',
            'email': 'koordinator.kmk@kmk.sch.id',
            'first_name': 'Koordinator',
            'last_name': 'KMK',
            'password': 'koordinator123',
            'role': 'koordinator_kmk',
            'is_staff': True,
            'is_superuser': False,
            'nip': 'KOR001',
            'phone': '08123456788'
        },
        {
            'username': 'kepala_madin',
            'email': 'kepala.madin@kmk.sch.id',
            'first_name': 'Kepala',
            'last_name': 'Madin',
            'password': 'kepala123',
            'role': 'kepala_madin',
            'is_staff': True,
            'is_superuser': False,
            'nip': 'KPL001',
            'phone': '08123456787'
        },
        {
            'username': 'muallimat_1',
            'email': 'muallimat1@kmk.sch.id',
            'first_name': 'Ahmad',
            'last_name': 'Rohman',
            'password': 'muallimat123',
            'role': 'muallimat',
            'is_staff': True,
            'is_superuser': False,
            'nip': 'MUA001',
            'phone': '08123456786'
        },
        {
            'username': 'muallimat_2',
            'email': 'muallimat2@kmk.sch.id',
            'first_name': 'Fatimah',
            'last_name': 'Azzahra',
            'password': 'muallimat123',
            'role': 'muallimat',
            'is_staff': True,
            'is_superuser': False,
            'nip': 'MUA002',
            'phone': '08123456785'
        }
    ]
    
    User = get_user_model()
    
    for user_data in users_data:
        username = user_data['username']
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            print(f"User '{username}' already exists!")
            continue
        
        try:
            # Create user
            user = User.objects.create_user(
                username=username,
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                password=user_data['password'],
                role=user_data['role'],
                is_staff=user_data['is_staff'],
                is_superuser=user_data['is_superuser'],
                nip=user_data['nip'],
                phone=user_data['phone']
            )
            
            print(f"User '{username}' created successfully!")
            print(f"   Role: {user.get_role_display()}")
            print(f"   Email: {user.email}")
            print(f"   NIP: {user.nip}")
            print(f"   Password: {user_data['password']}")
            print()
            
        except Exception as e:
            print(f"Error creating user '{username}': {e}")

if __name__ == '__main__':
    print("Creating role-based users...")
    create_role_users()
    print("\n=== Login Credentials ===")
    print("1. Admin Madin:")
    print("   Username: admin_madin")
    print("   Password: admin123")
    print("\n2. Koordinator KMK:")
    print("   Username: koordinator_kmk")
    print("   Password: koordinator123")
    print("\n3. Kepala Madin:")
    print("   Username: kepala_madin")
    print("   Password: kepala123")
    print("\n4. Muallimat 1:")
    print("   Username: muallimat_1")
    print("   Password: muallimat123")
    print("\n5. Muallimat 2:")
    print("   Username: muallimat_2")
    print("   Password: muallimat123")
    print("\n=== Access Rights Summary ===")
    print("• Admin Madin: Full access (user management, santri, classes, validation, settings)")
    print("• Koordinator KMK: Can manage santri, validate grades, manage settings")
    print("• Kepala Madin: Can view all classes")
    print("• Muallimat: Basic access (absensi, input nilai, dashboard, export)")
