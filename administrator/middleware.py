from django.shortcuts import redirect
from django.contrib import messages

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip middleware for admin URLs and static files
        if request.path.startswith('/admin/') or request.path.startswith('/static/') or request.path.startswith('/media/'):
            return self.get_response(request)

        # Skip for login/logout
        if request.path in ['/login/', '/logout/']:
            return self.get_response(request)

        # Check if user is authenticated
        if not request.user.is_authenticated:
            return self.get_response(request)

        # Define role-based access rules
        access_rules = {
            # User Management - hanya Admin Madin
            '/user/': ['admin_madin'],
            '/santri/tambah/': ['admin_madin', 'koordinator_kmk'],  # Data santri
            '/santri/edit/': ['admin_madin', 'koordinator_kmk'],
            '/santri/hapus/': ['admin_madin', 'koordinator_kmk'],
            
            # All Classes - Admin Diniyah, Koordinator KMK, Kepala Madin
            '/kelas/': ['admin_madin', 'koordinator_kmk', 'kepala_madin'],
            
            # Grade Validation - Admin Diniyah, Koordinator KMK
            '/nilai/validasi/': ['admin_madin', 'koordinator_kmk'],
            
            # Settings - Admin Diniyah, Koordinator KMK
            '/setting/': ['admin_madin', 'koordinator_kmk'],
        }

        # Check access for current path
        user_role = request.user.role
        for pattern, allowed_roles in access_rules.items():
            if request.path.startswith(pattern):
                if user_role not in allowed_roles:
                    messages.error(request, f'Akses ditolak. Role {request.user.get_role_display()} tidak memiliki izin untuk mengakses halaman ini.')
                    return redirect('dashboard')
                break

        response = self.get_response(request)
        return response
