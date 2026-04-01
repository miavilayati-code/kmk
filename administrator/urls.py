from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('santri/', views.santri_list, name='santri_list'),
    path('santri/tambah/', views.santri_tambah, name='santri_tambah'),
    path('santri/edit/<int:id>/', views.santri_edit, name='santri_edit'),
    path('santri/hapus/<int:id>/', views.santri_hapus, name='santri_hapus'),
    path('kelas/', views.kelas_list, name='kelas_list'),
    path('kelas/tambah/', views.kelas_tambah, name='kelas_tambah'),
    path('kelas/edit/<int:id>/', views.kelas_edit, name='kelas_edit'),
    path('kelas/hapus/<int:id>/', views.kelas_hapus, name='kelas_hapus'),
    path('cabang/', views.cabang_list, name='cabang_list'),
    path('cabang/tambah/', views.cabang_tambah, name='cabang_tambah'),
    path('cabang/edit/<int:id>/', views.cabang_edit, name='cabang_edit'),
    path('cabang/hapus/<int:id>/', views.cabang_hapus, name='cabang_hapus'),
    path('cabang/santri/<int:id>/', views.cabang_santri, name='cabang_santri'),
    path('tingkat/', views.tingkat_list, name='tingkat_list'),
    path('tingkat/tambah/', views.tingkat_tambah, name='tingkat_tambah'),
    path('tingkat/edit/<int:id>/', views.tingkat_edit, name='tingkat_edit'),
    path('tingkat/hapus/<int:id>/', views.tingkat_hapus, name='tingkat_hapus'),
    path('absensi/<int:jadwal_id>/', views.absensi_kelas, name='absensi_kelas'),
    path('absensi/', views.absensi_list, name='absensi_list'),
    path('jadwal/', views.daftar_jadwal, name='jadwal'),
    path('guru/', views.guru_list, name='guru_list'),
]