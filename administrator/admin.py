from django.contrib import admin
from .models import Cabang, Tingkat, Kelas, Santri, TahunAkademik, Semester, MataPelajaran, Guru, Jadwal, Absensi, Nilai



admin.site.register(Cabang)
admin.site.register(Tingkat)
admin.site.register(Kelas)
admin.site.register(Santri)

admin.site.register(TahunAkademik)
admin.site.register(Semester)
admin.site.register(MataPelajaran)
admin.site.register(Guru)
admin.site.register(Jadwal)
admin.site.register(Absensi)
admin.site.register(Nilai)