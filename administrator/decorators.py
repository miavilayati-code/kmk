from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def role_required(allowed_roles):
    """
    Decorator to restrict access based on user roles
    Usage: @role_required(['admin_madin', 'koordinator_kmk'])
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, 'Anda harus login terlebih dahulu.')
                return redirect('login')
            
            if request.user.role not in allowed_roles:
                user_role = request.user.get_role_display()
                messages.error(request, f'Akses ditolak. Role {user_role} tidak memiliki izin untuk mengakses halaman ini.')
                return redirect('dashboard')
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def admin_madin_required(view_func):
    """Decorator for Admin Madin only"""
    return role_required(['admin_madin'])(view_func)

def koordinator_kmk_required(view_func):
    """Decorator for Koordinator KMK only"""
    return role_required(['koordinator_kmk'])(view_func)

def kepala_madin_required(view_func):
    """Decorator for Kepala Madin only"""
    return role_required(['kepala_madin'])(view_func)

def management_required(view_func):
    """Decorator for Admin Madin and Koordinator KMK"""
    return role_required(['admin_madin', 'koordinator_kmk'])(view_func)

def validation_required(view_func):
    """Decorator for Admin Madin and Koordinator KMK (for grade validation)"""
    return role_required(['admin_madin', 'koordinator_kmk'])(view_func)

def settings_required(view_func):
    """Decorator for Admin Madin and Koordinator KMK (for settings)"""
    return role_required(['admin_madin', 'koordinator_kmk'])(view_func)

def all_management_required(view_func):
    """Decorator for Admin Madin, Koordinator KMK, and Kepala Madin"""
    return role_required(['admin_madin', 'koordinator_kmk', 'kepala_madin'])(view_func)
