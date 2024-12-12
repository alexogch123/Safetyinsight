# Generated by Django 3.2.23 on 2024-12-08 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_organization_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['nombre'], 'verbose_name': 'Organización', 'verbose_name_plural': 'Organizaciones'},
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('calle', models.CharField(help_text='Nombre de la calle', max_length=200)),
                ('numero_exterior', models.CharField(help_text='Número exterior', max_length=20)),
                ('numero_interior', models.CharField(blank=True, help_text='Número interior', max_length=20, null=True)),
                ('colonia', models.CharField(help_text='Nombre de la colonia', max_length=100)),
                ('codigo_postal', models.CharField(help_text='Código postal', max_length=10)),
                ('ciudad', models.CharField(help_text='Ciudad', max_length=100)),
                ('estado', models.CharField(help_text='Estado', max_length=100)),
                ('pais', models.CharField(default='México', help_text='País', max_length=100)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directions', to='company.organization')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Direcciones',
                'ordering': ['organization', 'calle'],
            },
        ),
    ]