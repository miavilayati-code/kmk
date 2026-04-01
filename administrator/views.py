from django.shortcuts import render, redirect, get_object_or_404
from .models import Santri, Kelas, Cabang, Absensi, Jadwal, Guru, Tingkat
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