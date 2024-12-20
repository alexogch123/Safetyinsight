# Generated by Django 3.2.23 on 2024-12-11 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0004_auto_20241207_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_organizations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='um',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='updated_organizations', to='auth.user'),
            preserve_default=False,
        ),
    ]
