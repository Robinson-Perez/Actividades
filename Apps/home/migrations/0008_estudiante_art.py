# Generated by Django 3.2.6 on 2021-09-10 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210910_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='art',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.articulo'),
        ),
    ]
