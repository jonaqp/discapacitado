# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-22 06:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteAdmision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('tipo_documento', models.CharField(choices=[('00', 'No Tiene'), ('01', 'DNI'), ('02', 'Carne Extranjeria'), ('04', 'Documento Identidad Extranjero')], default='01', max_length=10)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('numero_documento', models.CharField(default='', max_length=20, unique=True)),
                ('nombres', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('apellido_paterno', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('apellido_materno', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('genero', models.CharField(blank=True, choices=[('01', 'Masculino'), ('02', 'Femenino')], default='', max_length=2, null=True)),
                ('grado_instruccion', models.CharField(blank=True, choices=[('00', 'NINGUN NIVEL / ILETRADO'), ('01', 'INCIAL / PRE-ESCOLAR'), ('02', 'PRIMARIA INCOMPLETA'), ('03', 'PRIMARIA COMPLETA'), ('04', 'ESECUNDARIA INCOMPLETA'), ('05', 'SECUNDARIA COMPLETA'), ('06', 'SUPERIOR NO UNIV. INC.'), ('07', 'SUPERIOR NO UNIV. COMP.'), ('08', 'SUPERIOR UNIV. INC.'), ('09', 'SUPERIOR UNIV. COMP.')], max_length=10, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('financiador', models.CharField(blank=True, choices=[('00', 'NO SE CONOCE'), ('01', 'USUARIO'), ('02', 'SIS'), ('03', 'ESSALUD'), ('04', 'SOAT'), ('05', 'FINANCIADOR SANIDAD FAP'), ('06', 'SANIDAD NAVAL'), ('07', 'SANIDAD EP'), ('08', 'SANIDAD PNP'), ('09', 'PRIVADOS'), ('10', 'OTROS'), ('11', 'EXONERADO')], default='00', max_length=10, null=True)),
                ('numero_hci', models.CharField(blank=True, max_length=50, null=True)),
                ('etnia', models.CharField(blank=True, choices=[('01', 'AYMARA'), ('02', 'URO'), ('03', 'JAQARU, KAWI (JAQI, CAUQUI)'), ('04', 'CHANCAS'), ('05', 'CHOPCCAS'), ('06', "Q'EROS"), ('07', 'WANCAS'), ('08', 'OTROS GRUPOS QUECHUAS DEL AREA ANDINA (II)'), ('09', 'ACHUAR, ACHUAL'), ('10', 'AMAHUACA'), ('11', 'AMAIWERI • KISAMBAERI'), ('12', 'AMARA KAERI'), ('13', 'ANDOA - SHIMIGAE'), ('14', 'ANDOKE'), ('15', 'ARABELLA (CHIRUPINO)'), ('16', 'ARASAIRE'), ('17', 'ASHANINKA'), ('18', 'ASHENINKA'), ('19', 'AWAJUN (AGUARUNA, AENTS)'), ('20', 'BORA (MIAMUNA)'), ('21', 'CACATAIBO (UNI)'), ('22', 'CAHUARANA (MOROCANO)'), ('23', 'CANDOSHI - MURATO'), ('24', 'CAPANAHUA (JUNIKUIN)'), ('25', 'CAQUINTE (POYENISATI)'), ('26', 'CASHINAHUA (JUNIKUIN)'), ('27', 'CHAMICURO (CHAMEKOLO)'), ('28', 'CHITONAHUA'), ('29', 'COCAMA - COCAMILLA'), ('30', 'CUJARE—O (I—APARI)'), ('31', 'CULINA (MADIJA)'), ('32', 'ESE´EJA ("HUARAYO")'), ('33', 'HARAKMBUT'), ('34', 'HUACHIPAIRE'), ('35', 'HUAORANI (TAGAERI, TAROMENANE)'), ('36', 'HUITOTO (INCLUYE MURUI, MENECA, MUNAINE)'), ('37', 'IQUITO'), ('38', 'ISCONAHUA (ICOBAKEBO)'), ('39', 'JEBERO (SHIWIIU, SEWELO)'), ('40', 'JIBARO'), ('41', 'LAMISTO'), ('42', 'MACHIGUENGA (MATSIGENKA)'), ('43', 'MASHCO - PIRO ("MASHCO")'), ('44', 'MASTANAHUA'), ('45', 'MAYORUNA (MATS...)'), ('46', 'MURUNAHUA'), ('47', 'NANTI'), ('48', 'NOMATSIGUENGA'), ('49', 'OCAINA (IVOT´SA)'), ('50', 'OMAGUA'), ('51', 'OREJON (MAI HUNA, MAIJUNA)'), ('52', 'PISABO (MAYO, KANIBO)'), ('53', 'PUKIRIERI'), ('54', 'QUICHUA - QUICHUA RUNA, KICHWA (I)'), ('55', 'RESIGARO'), ('56', 'SAPITERI'), ('57', 'SECOYA (AIDO PAI)'), ('58', 'CHAPRA'), ('59', 'SHARANAHUA / MARINAHUA (ONIKOIN)'), ('60', 'SHAWI (CHAYAHUITA, KANPUNAN, KAMPU PIYAWI)'), ('61', 'SHIPIBO - CONIBO - SHETEBO'), ('62', 'SHUAR'), ('63', 'TAUSHIRO (PINCHE)'), ('64', 'TICUNA (DU<X<GU)'), ('65', 'TOYOERI'), ('66', 'URARINA (ITUKALE, SHIMACO, KACH¡)'), ('67', 'WAMPIS (HUAMBISA)'), ('68', 'YAGUA (YAWA, NIHAMWO)'), ('69', 'YAMINAHUA'), ('70', 'YANESHA ("AMUESHA")'), ('71', 'YINE • YAMI ("PIRO")'), ('72', 'YORA ("NAHUA", "PARQUENAHUA")'), ('73', 'OTROS GRUPOS INDIGENAS AMAZONICOS'), ('80', 'MESTIZO'), ('81', 'AFRO DESCENDIENTE'), ('82', 'ASIATICO DESCENDIENTE'), ('83', 'OTRO')], max_length=5, null=True)),
                ('componente_filiacion', models.CharField(blank=True, max_length=50, null=True)),
                ('codigo_componente_filiacion', models.CharField(blank=True, max_length=50, null=True)),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('distrito_residencial', models.CharField(blank=True, max_length=100, null=True)),
                ('distrito_residencial_actual', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion_actual', models.CharField(blank=True, max_length=100, null=True)),
                ('referencia', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono_movil', models.CharField(blank=True, max_length=10, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': '1. Paciente Admision',
            },
        ),
        migrations.CreateModel(
            name='PacienteAtencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('ayuda_tecnica', models.CharField(blank=True, max_length=10, null=True)),
                ('accidente_dano', models.CharField(blank=True, max_length=10, null=True)),
                ('tiempo_discapacidad_anio', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('tiempo_discapacidad_mes', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('tiempo_discapacidad_dia', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('tstdd_anio', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('tstdd_mes', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('tstdd_dia', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('is_discapacidad_nacido', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '5. Paciente Atencion',
            },
        ),
        migrations.CreateModel(
            name='PacienteCIEX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('codigo_ciex', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': '6. Paciente CIEX',
            },
        ),
        migrations.CreateModel(
            name='PacienteCIF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('codigo_cif', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': '9. Paciente CIF',
            },
        ),
        migrations.CreateModel(
            name='PacienteCita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('area', models.CharField(choices=[('01', 'Discapacidad y Rehabilitacion')], default='01', max_length=10)),
                ('tipo_atencion', models.CharField(choices=[('01', 'Atendido'), ('02', 'En Espera'), ('03', 'Cancelado')], default='02', max_length=10)),
            ],
            options={
                'verbose_name_plural': '2. Paciente Cita',
            },
        ),
        migrations.CreateModel(
            name='PacienteCondicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('en_establecimiento', models.CharField(blank=True, choices=[('01', 'Nuevo'), ('02', 'Continuador')], default='01', max_length=10, null=True)),
                ('referencia_establecimiento', models.CharField(blank=True, choices=[('00', 'Nulo'), ('01', 'Iniciativa Propia')], default='00', max_length=10, null=True)),
                ('en_servicio', models.CharField(blank=True, choices=[('01', 'Nuevo'), ('02', 'Continuador')], default='01', max_length=10, null=True)),
                ('establecimiento_servicio', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': '4. Paciente Condicion',
            },
        ),
        migrations.CreateModel(
            name='PacienteConsulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('fecha', models.DateField()),
                ('numero_terapia', models.PositiveSmallIntegerField(default=0)),
                ('descripcion_terapia', models.TextField(blank=True, null=True)),
                ('observacion_terapia', models.TextField(blank=True, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_pacienteconsulta_paciente_cita', to='paciente.PacienteCita')),
                ('usuario_creacion', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paciente_pacienteconsulta_usuario_creacion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '3. Paciente Consulta',
            },
        ),
        migrations.CreateModel(
            name='PacienteDeficiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('codigo_deficiencia', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=200)),
                ('gravedad', models.CharField(max_length=10)),
                ('paciente_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_pacientedeficiencia_paciente_consulta', to='paciente.PacienteConsulta')),
                ('usuario_creacion', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paciente_pacientedeficiencia_usuario_creacion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '7. Paciente Deficiencia',
            },
        ),
        migrations.CreateModel(
            name='PacienteDiscapacidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('codigo_discapacidad', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=200)),
                ('paciente_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_pacientediscapacidad_paciente_consulta', to='paciente.PacienteConsulta')),
                ('usuario_creacion', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paciente_pacientediscapacidad_usuario_creacion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '8. Paciente Capacidad',
            },
        ),
        migrations.CreateModel(
            name='PacienteProcedimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('codigo_cpt', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=200)),
                ('paciente_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_pacienteprocedimiento_paciente_consulta', to='paciente.PacienteConsulta')),
                ('usuario_creacion', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paciente_pacienteprocedimiento_usuario_creacion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '10. Paciente Procedimiento',
            },
        ),
        migrations.AddField(
            model_name='pacientecondicion',
            name='paciente_consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_pacientecondicion_paciente_consulta', to='paciente.PacienteConsulta'),
        ),
        migrations.AddField(
            model_name='pacientecondicion',
            name='usuario_creacion',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paciente_pacientecondicion_usuario_creacion', to=settings.AUTH_USER_MODEL),
        ),
    ]
