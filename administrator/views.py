from django.shortcuts import render, redirect, get_object_or_404
from .models import Santri, Kelas, Cabang, Absensi, Jadwal, Guru
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

        kelas_obj = Kelas.objects.get(id=kelas_id)

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
    santri = Santri.objects.get(id=id)
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
    santri = Santri.objects.get(id=id)
    santri.delete()

    return redirect('santri_list')


def absensi_kelas(request, jadwal_id):
    jadwal = get_object_or_404(Jadwal, id=jadwal_id)
    santri = Santri.objects.filter(kelas=jadwal.kelas)

    if request.method == "POST":

        for s in santri:

            status = request.POST.get(f"status_{s.id}")

            Absensi.objects.create(
                santri=s,
                jadwal=jadwal,
                status=status
            )

        return redirect('jadwal')

    context = {
        'jadwal': jadwal,
        'santri': santri
    }

    return render(request, 'absensi/absensi_kelas.html', context)

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