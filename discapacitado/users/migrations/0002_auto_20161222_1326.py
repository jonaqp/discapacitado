# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-22 13:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0001_initial'),
        ('common', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('fecha', models.DateField(help_text='fecha empezando el mes, ejemplo:2016-11-01')),
                ('cupo', models.PositiveSmallIntegerField(default=10)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_usercupo_establecimiento', to='establecimiento.Establecimiento')),
            ],
            options={
                'verbose_name_plural': '3. Usuarios Cupos',
            },
        ),
        migrations.CreateModel(
            name='UserDisponibilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('horario', models.DateTimeField()),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_userdisponibilidad_establecimiento', to='establecimiento.Establecimiento')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_userdisponibilidad_turno', to='common.Turno')),
            ],
            options={
                'verbose_name_plural': '4. Usuario Disponibilidades',
            },
        ),
        migrations.CreateModel(
            name='UserEstablecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('establecimiento', models.ManyToManyField(related_name='users_userestablecimiento_establecimiento', to='establecimiento.Establecimiento')),
            ],
            options={
                'verbose_name_plural': '2. Usuarios Establecimientos',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': '1. Usuarios'},
        ),
        migrations.AddField(
            model_name='userestablecimiento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_userestablecimiento_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userestablecimiento',
            name='usuario_creacion',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_userestablecimiento_usuario_creacion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userdisponibilidad',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_userdisponibilidad_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userdisponibilidad',
            name='usuario_creacion',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_userdisponibilidad_usuario_creacion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercupo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_usercupo_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercupo',
            name='usuario_creacion',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_usercupo_usuario_creacion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userestablecimiento',
            unique_together=set([('usuario',)]),
        ),
        migrations.AlterUniqueTogether(
            name='userdisponibilidad',
            unique_together=set([('usuario', 'turno', 'horario', 'establecimiento')]),
        ),
        migrations.AlterUniqueTogether(
            name='usercupo',
            unique_together=set([('usuario', 'fecha', 'cupo', 'establecimiento')]),
        ),
    ]
