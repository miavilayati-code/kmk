#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmk.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin_user():
    username = 'admin'
    email = 'admin@kmk.sch.id'
    password = 'admin123'
    
    # Check if user already exists
    if User.objects.filter(username=username).exists():
        print(f"User '{username}' already exists!")
        return False
    
    # Create superuser
    try:
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"Admin user created successfully!")
        print(f"   Username: {username}")
        print(f"   Password: {password}")
        print(f"   Email: {email}")
        return True
    except Exception as e:
        print(f"Error creating admin user: {e}")
        return False

if __name__ == '__main__':
    print("Creating admin user...")
    create_admin_user()
