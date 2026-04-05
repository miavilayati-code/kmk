from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .decorators import admin_madin_required
from .forms import UserCreationForm, UserEditForm

@login_required
@admin_madin_required
def user_list(request):
    """Daftar pengguna - hanya Admin Madin"""
    search = request.GET.get('search', '')
    role_filter = request.GET.get('role', '')
    
    users = User.objects.all().order_by('-date_joined')
    
    if search:
        users = users.filter(
            Q(username__icontains=search) |
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search)
        )
    
    if role_filter:
        users = users.filter(role=role_filter)
    
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search': search,
        'role_filter': role_filter,
        'role_choices': User.ROLE_CHOICES,
    }
    
    return render(request, 'user/list.html', context)

@login_required
@admin_madin_required
def user_tambah(request):
    """Tambah pengguna - hanya Admin Madin"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Pengguna {user.username} berhasil ditambahkan.')
            return redirect('user_list')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
        'title': 'Tambah Pengguna',
    }
    
    return render(request, 'user/form.html', context)

@login_required
@admin_madin_required
def user_edit(request, id):
    """Edit pengguna - hanya Admin Madin"""
    user = get_object_or_404(User, id=id)
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Pengguna {user.username} berhasil diperbarui.')
            return redirect('user_list')
    else:
        form = UserEditForm(instance=user)
    
    context = {
        'form': form,
        'user': user,
        'title': 'Edit Pengguna',
    }
    
    return render(request, 'user/form.html', context)

@login_required
@admin_madin_required
def user_hapus(request, id):
    """Hapus pengguna - hanya Admin Madin"""
    user = get_object_or_404(User, id=id)
    
    if request.method == 'POST':
        username = user.username
        user.delete()
        messages.success(request, f'Pengguna {username} berhasil dihapus.')
        return redirect('user_list')
    
    context = {
        'user': user,
        'title': 'Hapus Pengguna',
    }
    
    return render(request, 'user/hapus.html', context)

@login_required
def user_detail(request, id):
    """Detail pengguna - semua user bisa lihat detail user lain"""
    user = get_object_or_404(User, id=id)
    
    context = {
        'user': user,
        'title': 'Detail Pengguna',
    }
    
    return render(request, 'user/detail.html', context)
