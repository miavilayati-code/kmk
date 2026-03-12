from django.db import models

class Cabang(models.Model):
    nama_cabang = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Cabang"
        verbose_name_plural = "Cabang"

    def __str__(self):
        return self.nama_cabang
    
class Tingkat(models.Model):
    nama_tingkat = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tingkat"
        verbose_name_plural = "Tingkat"

    def __str__(self):
        return self.nama_tingkat

class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=50)
    cabang = models.ForeignKey(Cabang, on_delete=models.CASCADE)
    tingkat = models.ForeignKey(Tingkat, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Kelas"
        verbose_name_plural = "Kelas"

    def __str__(self):
        return f"{self.nama_kelas} - {self.tingkat}"

class Santri(models.Model):
    nama = models.CharField(max_length=100)
    nis = models.CharField(max_length=20)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)  

    class Meta:
        verbose_name = "Santri"
        verbose_name_plural = "Santri"

    def __str__(self):
        return self.nama

class TahunAkademik(models.Model):
    tahun = models.CharField(max_length=9)  # contoh: 2025/2026
    aktif = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tahun Akademik"
        verbose_name_plural = "Tahun Akademik"

    def __str__(self):
        return self.tahun
    
class Semester(models.Model):
    nama_semester = models.CharField(max_length=20)  # Ganjil / Genap
    tahun_akademik = models.ForeignKey(TahunAkademik, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Semester"
        verbose_name_plural = "Semester"

    def __str__(self):
        return f"{self.nama_semester} - {self.tahun_akademik}"
    
class MataPelajaran(models.Model):
    nama_mapel = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Mata Pelajaran"
        verbose_name_plural = "Mata Pelajaran"

    def __str__(self):
        return self.nama_mapel

class Guru(models.Model):
    nama_guru = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Guru"
        verbose_name_plural = "Guru"

    def __str__(self):
        return self.nama_guru
    
class Jadwal(models.Model):
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE, null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    hari = models.CharField(max_length=20)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()

    class Meta:
        verbose_name = "Jadwal"
        verbose_name_plural = "Jadwal"

    def __str__(self):
        return f"{self.kelas} - {self.mata_pelajaran} - {self.guru}"
    
class Absensi(models.Model):
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE)
    jadwal = models.ForeignKey(Jadwal, on_delete=models.CASCADE)
    tanggal = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('Hadir', 'Hadir'),
            ('Izin', 'Izin'),
            ('Sakit', 'Sakit'),
            ('Alfa', 'Alfa'),
        ]
    )

    class Meta:
        verbose_name = "Absensi"
        verbose_name_plural = "Absensi"

    def __str__(self):
        return f"{self.santri} - {self.tanggal}"
    
class Nilai(models.Model):
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    nilai = models.IntegerField()

    class Meta:
        verbose_name = "Nilai"
        verbose_name_plural = "Nilai"

    def __str__(self):
        return f"{self.santri} - {self.nilai}"

