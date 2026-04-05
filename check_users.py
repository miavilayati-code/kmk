#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmk.settings')
django.setup()

from django.contrib.auth.models import User

def check_users():
    users = User.objects.all()
    
    print("=== All Users in Database ===")
    if not users:
        print("No users found in database!")
        return
    
    for user in users:
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Staff: {user.is_staff}")
        print(f"Superuser: {user.is_superuser}")
        print(f"Active: {user.is_active}")
        print("-" * 30)

if __name__ == '__main__':
    check_users()
