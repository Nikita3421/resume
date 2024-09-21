# Generated by Django 5.0.7 on 2024-08-04 09:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('birth_date', models.DateField()),
                ('birth_place', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('residance_address', models.TextField()),
                ('tel_num', models.IntegerField()),
                ('email', models.EmailField(max_length=511)),
                ('studying', models.TextField()),
                ('work_exp', models.TextField()),
                ('knowladge', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=511)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField(auto_now_add=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='Resume.resume')),
            ],
        ),
    ]
