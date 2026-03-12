from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('santri/', views.santri_list, name='santri_list'),
    path('santri/tambah/', views.santri_tambah, name='santri_tambah'),
    path('santri/edit/<int:id>/', views.santri_edit, name='santri_edit'),
    path('santri/hapus/<int:id>/', views.santri_hapus, name='santri_hapus'),
    path('absensi/<int:jadwal_id>/', views.absensi_kelas, name='absensi_kelas'),
    path('absensi/', views.absensi_list, name='absensi_list'),
    path('jadwal/', views.daftar_jadwal, name='jadwal'),
    path('guru/', views.guru_list, name='guru_list'),
]