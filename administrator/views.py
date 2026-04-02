from django.shortcuts import render, redirect, get_object_or_404
from .models import Santri, Kelas, Cabang, Absensi, Jadwal, Guru, Tingkat, MataPelajaran, Semester, TahunAkademik
from datetime import date

def dashboard(request):
    jumlah_santri = Santri.objects.count()
    jumlah_kelas = Kelas.objects.count()
    jumlah_cabang = Cabang.objects.count()

    context = {
        'santri': jumlah_santri,
        'kelas': jumlah_kelas,
        'cabang': jumlah_cabang,
    }

    return render(request, 'dashboard.html', context)


def santri_list(request):
    data_santri = Santri.objects.all()
    context = {
        'santri': data_santri
    }
    return render(request, 'santri/list.html', context)


def santri_tambah(request):
    kelas = Kelas.objects.all()

    if request.method == 'POST':

        nama = request.POST['nama']
        nis = request.POST['nis']
        kelas_id = request.POST['kelas']

        kelas_obj = get_object_or_404(Kelas, id=kelas_id)

        Santri.objects.create(
            nama=nama,
            nis=nis,
            kelas=kelas_obj
        )

        return redirect('santri_list')

    context = {
        'kelas': kelas
    }

    return render(request, 'santri/tambah.html', context)


def santri_edit(request, id):
    santri = get_object_or_404(Santri, id=id)
    kelas = Kelas.objects.all()

    if request.method == 'POST':

        santri.nama = request.POST['nama']
        santri.nis = request.POST['nis']
        santri.kelas_id = request.POST['kelas']

        santri.save()

        return redirect('santri_list')

    context = {
        'data': santri,
        'kelas': kelas
    }

    return render(request, 'santri/edit.html', context)

def santri_hapus(request, id):
    santri = get_object_or_404(Santri, id=id)
    santri.delete()

    return redirect('santri_list')


def absensi_kelas(request, jadwal_id):
    jadwal = get_object_or_404(Jadwal, id=jadwal_id)
    santri = Santri.objects.filter(kelas=jadwal.kelas)

    # ✅ Ambil absensi hari ini
    absensi_hari_ini = Absensi.objects.filter(
        jadwal=jadwal,
        tanggal=date.today()
    )

    # ✅ Jadikan dictionary
    absensi_dict = {
        a.santri.id: a.status
        for a in absensi_hari_ini
    }

    if request.method == "POST":
        for s in santri:
            status = request.POST.get(f"status_{s.id}")

            if status:
                Absensi.objects.update_or_create(
                    santri=s,
                    jadwal=jadwal,
                    tanggal=date.today(),
                    defaults={'status': status}
                )

        return redirect('absensi_kelas', jadwal_id=jadwal.id)

    context = {
        'jadwal': jadwal,
        'santri': santri,   # 🔥 konsisten pakai list
        'absensi_dict': absensi_dict
    }

    return render(request, 'absensi/absensi_kelas.html', context)

# def absensi_kelas(request, jadwal_id):
#     jadwal = get_object_or_404(Jadwal, id=jadwal_id)
#     santri = Santri.objects.all()

#     if request.method == 'POST':
#         for santri in santri:
#             status = request.POST.get(f'status_{santri.id}')

#             if status:
#                 Absensi.objects.update_or_create(
#                     santri=santri,
#                     jadwal=jadwal,
#                     tanggal=date.today(),
#                     defaults={'status': status}
#                 )

#         return redirect('absensi_kelas', jadwal_id=jadwal.id)

#     return render(request, 'absensi/absensi_kelas.html', {
#         'jadwal': jadwal,
#         'santri': santri
#     })

def daftar_jadwal(request):
    jadwal = Jadwal.objects.select_related('kelas','mata_pelajaran','semester').all()

    context = {
        'jadwal': jadwal
    }

    return render(request, 'jadwal/daftar_jadwal.html', context)

def jadwal_tambah(request):
    kelas = Kelas.objects.select_related('cabang', 'tingkat').all()
    mata_pelajaran = MataPelajaran.objects.all()
    guru = Guru.objects.all()
    semester = Semester.objects.select_related('tahun_akademik').all()
    
    if request.method == 'POST':
        kelas_id = request.POST['kelas']
        mata_pelajaran_id = request.POST['mata_pelajaran']
        guru_id = request.POST['guru']
        semester_id = request.POST['semester']
        hari = request.POST['hari']
        jam_mulai = request.POST['jam_mulai']
        jam_selesai = request.POST['jam_selesai']
        
        kelas_obj = get_object_or_404(Kelas, id=kelas_id)
        mata_pelajaran_obj = get_object_or_404(MataPelajaran, id=mata_pelajaran_id)
        guru_obj = get_object_or_404(Guru, id=guru_id) if guru_id else None
        semester_obj = get_object_or_404(Semester, id=semester_id)
        
        Jadwal.objects.create(
            kelas=kelas_obj,
            mata_pelajaran=mata_pelajaran_obj,
            guru=guru_obj,
            semester=semester_obj,
            hari=hari,
            jam_mulai=jam_mulai,
            jam_selesai=jam_selesai
        )
        
        return redirect('jadwal')
    
    context = {
        'kelas': kelas,
        'mata_pelajaran': mata_pelajaran,
        'guru': guru,
        'semester': semester
    }
    
    return render(request, 'jadwal/tambah.html', context)


def jadwal_edit(request, id):
    jadwal = get_object_or_404(Jadwal, id=id)
    kelas = Kelas.objects.select_related('cabang', 'tingkat').all()
    mata_pelajaran = MataPelajaran.objects.all()
    guru = Guru.objects.all()
    semester = Semester.objects.select_related('tahun_akademik').all()
    
    if request.method == 'POST':
        jadwal.kelas_id = request.POST['kelas']
        jadwal.mata_pelajaran_id = request.POST['mata_pelajaran']
        guru_id = request.POST['guru']
        jadwal.guru_id = guru_id if guru_id else None
        jadwal.semester_id = request.POST['semester']
        jadwal.hari = request.POST['hari']
        jadwal.jam_mulai = request.POST['jam_mulai']
        jadwal.jam_selesai = request.POST['jam_selesai']
        
        jadwal.save()
        
        return redirect('jadwal')
    
    context = {
        'data': jadwal,
        'kelas': kelas,
        'mata_pelajaran': mata_pelajaran,
        'guru': guru,
        'semester': semester
    }
    
    return render(request, 'jadwal/edit.html', context)


def jadwal_hapus(request, id):
    jadwal = get_object_or_404(Jadwal, id=id)
    jadwal.delete()
    
    return redirect('jadwal')

def absensi_list(request):
    jadwal = Jadwal.objects.all()

    context = {
        'jadwal': jadwal
    }

    return render(request, 'absensi/absensi_list.html', context)

def guru_list(request):
    guru = Guru.objects.all()

    context = {
        'guru': guru
    }

    return render(request, 'guru/guru_list.html', context)


def guru_tambah(request):
    if request.method == 'POST':
        nama_guru = request.POST['nama_guru']
        
        Guru.objects.create(nama_guru=nama_guru)
        
        return redirect('guru_list')
    
    return render(request, 'guru/tambah.html')


def guru_edit(request, id):
    guru = get_object_or_404(Guru, id=id)
    
    if request.method == 'POST':
        guru.nama_guru = request.POST['nama_guru']
        guru.save()
        
        return redirect('guru_list')
    
    context = {
        'data': guru
    }
    
    return render(request, 'guru/edit.html', context)


def guru_hapus(request, id):
    guru = get_object_or_404(Guru, id=id)
    guru.delete()
    
    return redirect('guru_list')


def kelas_list(request):
    kelas = Kelas.objects.select_related('cabang', 'tingkat').all()
    
    context = {
        'kelas': kelas
    }
    
    return render(request, 'kelas/list.html', context)


def kelas_tambah(request):
    cabang = Cabang.objects.all()
    tingkat = Tingkat.objects.all()
    
    if request.method == 'POST':
        nama_kelas = request.POST['nama_kelas']
        cabang_id = request.POST['cabang']
        tingkat_id = request.POST['tingkat']
        
        cabang_obj = get_object_or_404(Cabang, id=cabang_id)
        tingkat_obj = get_object_or_404(Tingkat, id=tingkat_id)
        
        Kelas.objects.create(
            nama_kelas=nama_kelas,
            cabang=cabang_obj,
            tingkat=tingkat_obj
        )
        
        return redirect('kelas_list')
    
    context = {
        'cabang': cabang,
        'tingkat': tingkat
    }
    
    return render(request, 'kelas/tambah.html', context)


def kelas_edit(request, id):
    kelas = get_object_or_404(Kelas, id=id)
    cabang = Cabang.objects.all()
    tingkat = Tingkat.objects.all()
    
    if request.method == 'POST':
        kelas.nama_kelas = request.POST['nama_kelas']
        kelas.cabang_id = request.POST['cabang']
        kelas.tingkat_id = request.POST['tingkat']
        
        kelas.save()
        
        return redirect('kelas_list')
    
    context = {
        'data': kelas,
        'cabang': cabang,
        'tingkat': tingkat
    }
    
    return render(request, 'kelas/edit.html', context)


def kelas_hapus(request, id):
    kelas = get_object_or_404(Kelas, id=id)
    kelas.delete()
    
    return redirect('kelas_list')


def cabang_list(request):
    cabang = Cabang.objects.all()
    
    # Tambahkan jumlah santri per cabang
    cabang_with_count = []
    for item in cabang:
        santri_count = Santri.objects.filter(kelas__cabang=item).count()
        cabang_with_count.append({
            'cabang': item,
            'santri_count': santri_count
        })
    
    context = {
        'cabang_data': cabang_with_count
    }
    
    return render(request, 'cabang/list.html', context)


def cabang_tambah(request):
    if request.method == 'POST':
        nama_cabang = request.POST['nama_cabang']
        
        Cabang.objects.create(nama_cabang=nama_cabang)
        
        return redirect('cabang_list')
    
    return render(request, 'cabang/tambah.html')


def cabang_edit(request, id):
    cabang = get_object_or_404(Cabang, id=id)
    
    if request.method == 'POST':
        cabang.nama_cabang = request.POST['nama_cabang']
        cabang.save()
        
        return redirect('cabang_list')
    
    context = {
        'data': cabang
    }
    
    return render(request, 'cabang/edit.html', context)


def cabang_hapus(request, id):
    cabang = get_object_or_404(Cabang, id=id)
    cabang.delete()
    
    return redirect('cabang_list')


def cabang_santri(request, id):
    cabang = get_object_or_404(Cabang, id=id)
    santri = Santri.objects.select_related('kelas').filter(kelas__cabang=cabang)
    
    context = {
        'cabang': cabang,
        'santri': santri
    }
    
    return render(request, 'cabang/santri.html', context)


def tingkat_list(request):
    tingkat = Tingkat.objects.all()
    
    context = {
        'tingkat': tingkat
    }
    
    return render(request, 'tingkat/list.html', context)


def tingkat_tambah(request):
    if request.method == 'POST':
        nama_tingkat = request.POST['nama_tingkat']
        
        Tingkat.objects.create(nama_tingkat=nama_tingkat)
        
        return redirect('tingkat_list')
    
    return render(request, 'tingkat/tambah.html')


def tingkat_edit(request, id):
    tingkat = get_object_or_404(Tingkat, id=id)
    
    if request.method == 'POST':
        tingkat.nama_tingkat = request.POST['nama_tingkat']
        tingkat.save()
        
        return redirect('tingkat_list')
    
    context = {
        'data': tingkat
    }
    
    return render(request, 'tingkat/edit.html', context)


def tingkat_hapus(request, id):
    tingkat = get_object_or_404(Tingkat, id=id)
    tingkat.delete()
    
    return redirect('tingkat_list')


def mata_pelajaran_list(request):
    mata_pelajaran = MataPelajaran.objects.all()
    
    context = {
        'mata_pelajaran': mata_pelajaran
    }
    
    return render(request, 'mata_pelajaran/list.html', context)


def mata_pelajaran_tambah(request):
    if request.method == 'POST':
        nama_mapel = request.POST['nama_mapel']
        
        MataPelajaran.objects.create(nama_mapel=nama_mapel)
        
        return redirect('mata_pelajaran_list')
    
    return render(request, 'mata_pelajaran/tambah.html')


def mata_pelajaran_edit(request, id):
    mata_pelajaran = get_object_or_404(MataPelajaran, id=id)
    
    if request.method == 'POST':
        mata_pelajaran.nama_mapel = request.POST['nama_mapel']
        mata_pelajaran.save()
        
        return redirect('mata_pelajaran_list')
    
    context = {
        'data': mata_pelajaran
    }
    
    return render(request, 'mata_pelajaran/edit.html', context)


def mata_pelajaran_hapus(request, id):
    mata_pelajaran = get_object_or_404(MataPelajaran, id=id)
    mata_pelajaran.delete()
    
    return redirect('mata_pelajaran_list')


def tahun_akademik_list(request):
    tahun_akademik = TahunAkademik.objects.all()
    
    context = {
        'tahun_akademik': tahun_akademik
    }
    
    return render(request, 'tahun_akademik/list.html', context)


def tahun_akademik_tambah(request):
    if request.method == 'POST':
        tahun = request.POST['tahun']
        aktif = request.POST.get('aktif', False)
        
        TahunAkademik.objects.create(tahun=tahun, aktif=aktif)
        
        return redirect('tahun_akademik_list')
    
    return render(request, 'tahun_akademik/tambah.html')


def tahun_akademik_edit(request, id):
    tahun_akademik = get_object_or_404(TahunAkademik, id=id)
    
    if request.method == 'POST':
        tahun_akademik.tahun = request.POST['tahun']
        tahun_akademik.aktif = request.POST.get('aktif', False)
        tahun_akademik.save()
        
        return redirect('tahun_akademik_list')
    
    context = {
        'data': tahun_akademik
    }
    
    return render(request, 'tahun_akademik/edit.html', context)


def tahun_akademik_hapus(request, id):
    tahun_akademik = get_object_or_404(TahunAkademik, id=id)
    tahun_akademik.delete()
    
    return redirect('tahun_akademik_list')


def semester_list(request):
    semester = Semester.objects.select_related('tahun_akademik').all()
    
    context = {
        'semester': semester
    }
    
    return render(request, 'semester/list.html', context)


def semester_tambah(request):
    tahun_akademik = TahunAkademik.objects.all()
    
    if request.method == 'POST':
        nama_semester = request.POST['nama_semester']
        tahun_akademik_id = request.POST['tahun_akademik']
        
        tahun_akademik_obj = get_object_or_404(TahunAkademik, id=tahun_akademik_id)
        
        Semester.objects.create(
            nama_semester=nama_semester,
            tahun_akademik=tahun_akademik_obj
        )
        
        return redirect('semester_list')
    
    context = {
        'tahun_akademik': tahun_akademik
    }
    
    return render(request, 'semester/tambah.html', context)


def semester_edit(request, id):
    semester = get_object_or_404(Semester, id=id)
    tahun_akademik = TahunAkademik.objects.all()
    
    if request.method == 'POST':
        semester.nama_semester = request.POST['nama_semester']
        semester.tahun_akademik_id = request.POST['tahun_akademik']
        semester.save()
        
        return redirect('semester_list')
    
    context = {
        'data': semester,
        'tahun_akademik': tahun_akademik
    }
    
    return render(request, 'semester/edit.html', context)


def semester_hapus(request, id):
    semester = get_object_or_404(Semester, id=id)
    semester.delete()
    
    return redirect('semester_list')