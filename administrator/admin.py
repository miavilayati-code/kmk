from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Cabang, Tingkat, Kelas, Santri, TahunAkademik, Semester, MataPelajaran, Guru, Jadwal, Absensi, Nilai

@admin.register(Cabang)
class CabangAdmin(admin.ModelAdmin):
    list_display = ('nama_cabang',)
    search_fields = ('nama_cabang',)
    ordering = ('nama_cabang',)

@admin.register(Tingkat)
class TingkatAdmin(admin.ModelAdmin):
    list_display = ('nama_tingkat',)
    search_fields = ('nama_tingkat',)
    ordering = ('nama_tingkat',)

@admin.register(Kelas)
class KelasAdmin(admin.ModelAdmin):
    list_display = ('nama_kelas', 'tingkat', 'cabang')
    list_filter = ('tingkat', 'cabang')
    search_fields = ('nama_kelas',)
    ordering = ('nama_kelas',)

@admin.register(TahunAkademik)
class TahunAkademikAdmin(admin.ModelAdmin):
    list_display = ('tahun', 'aktif')
    list_filter = ('aktif',)
    search_fields = ('tahun',)
    ordering = ('tahun',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('nama_semester', 'tahun_akademik')
    list_filter = ('nama_semester', 'tahun_akademik')
    search_fields = ('nama_semester',)
    ordering = ('tahun_akademik', 'nama_semester')

@admin.register(Santri)
class SantriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nis', 'kelas')
    list_filter = ('kelas',)
    search_fields = ('nama', 'nis')
    ordering = ('nama',)

@admin.register(Guru)
class GuruAdmin(admin.ModelAdmin):
    list_display = ('nama_guru',)
    search_fields = ('nama_guru',)
    ordering = ('nama_guru',)

@admin.register(MataPelajaran)
class MataPelajaranAdmin(admin.ModelAdmin):
    list_display = ('nama_mapel',)
    search_fields = ('nama_mapel',)
    ordering = ('nama_mapel',)

@admin.register(Jadwal)
class JadwalAdmin(admin.ModelAdmin):
    list_display = ('hari', 'jam_mulai', 'jam_selesai', 'mata_pelajaran', 'guru', 'kelas', 'semester')
    list_filter = ('hari', 'semester')
    search_fields = ('mata_pelajaran__nama_mapel', 'guru__nama_guru', 'kelas__nama_kelas')
    ordering = ('hari', 'jam_mulai')
    raw_id_fields = ('mata_pelajaran', 'guru', 'kelas', 'semester')

@admin.register(Absensi)
class AbsensiAdmin(admin.ModelAdmin):
    list_display = ('santri', 'jadwal', 'tanggal', 'status')
    list_filter = ('status', 'tanggal')
    search_fields = ('santri__nama', 'jadwal__mata_pelajaran__nama_mapel')
    ordering = ('-tanggal',)
    date_hierarchy = 'tanggal'

@admin.register(Nilai)
class NilaiAdmin(admin.ModelAdmin):
    list_display = ('santri', 'mata_pelajaran', 'semester', 'nilai')
    list_filter = ('semester',)
    search_fields = ('santri__nama', 'mata_pelajaran__nama_mapel')
    ordering = ('-semester', 'santri__nama', 'mata_pelajaran__nama_mapel')
    raw_id_fields = ('santri', 'mata_pelajaran', 'semester')