from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect

class RoleRequiredMixin(UserPassesTestMixin):
    """Mixin to restrict access based on user roles"""
    allowed_roles = []
    
    def test_func(self, user):
        if not user.is_authenticated:
            return False
        return user.role in self.allowed_roles
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Anda harus login terlebih dahulu.')
            return redirect('login')
        
        user_role = self.request.user.get_role_display()
        messages.error(self.request, f'Akses ditolak. Role {user_role} tidak memiliki izin untuk mengakses halaman ini.')
        return redirect('dashboard')

class AdminMadinRequiredMixin(RoleRequiredMixin):
    """Mixin for Admin Madin only"""
    allowed_roles = ['admin_madin']

class KoordinatorKMKRequiredMixin(RoleRequiredMixin):
    """Mixin for Koordinator KMK only"""
    allowed_roles = ['koordinator_kmk']

class KepalaMadinRequiredMixin(RoleRequiredMixin):
    """Mixin for Kepala Madin only"""
    allowed_roles = ['kepala_madin']

class ManagementRequiredMixin(RoleRequiredMixin):
    """Mixin for Admin Madin and Koordinator KMK"""
    allowed_roles = ['admin_madin', 'koordinator_kmk']

class ValidationRequiredMixin(RoleRequiredMixin):
    """Mixin for Admin Madin and Koordinator KMK (for grade validation)"""
    allowed_roles = ['admin_madin', 'koordinator_kmk']

class SettingsRequiredMixin(RoleRequiredMixin):
    """Mixin for Admin Madin and Koordinator KMK (for settings)"""
    allowed_roles = ['admin_madin', 'koordinator_kmk']

class AllManagementRequiredMixin(RoleRequiredMixin):
    """Mixin for Admin Madin, Koordinator KMK, and Kepala Madin"""
    allowed_roles = ['admin_madin', 'koordinator_kmk', 'kepala_madin']

class AnyAuthenticatedRequiredMixin(RoleRequiredMixin):
    """Mixin for any authenticated user"""
    allowed_roles = ['admin_madin', 'koordinator_kmk', 'kepala_madin', 'muallimat']
