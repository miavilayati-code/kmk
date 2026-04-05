# Generated migration to create missing tables

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=10)),
                ('jam_mulai', models.TimeField()),
                ('jam_selesai', models.TimeField()),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.matapelajaran')),
                ('guru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.guru')),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.kelas')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.semester')),
            ],
            options={
                'verbose_name': 'Jadwal',
                'verbose_name_plural': 'Jadwal',
            },
        ),
        migrations.CreateModel(
            name='Absensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('santri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.santri')),
                ('jadwal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.jadwal')),
                ('tanggal', models.DateField()),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Absensi',
                'verbose_name_plural': 'Absensi',
            },
        ),
        migrations.CreateModel(
            name='Nilai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('santri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.santri')),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.matapelajaran')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.semester')),
                ('nilai', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Nilai',
                'verbose_name_plural': 'Nilai',
            },
        ),
    ]
