# Generated by Django 3.2.6 on 2021-11-02 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alexadashcams', '0011_auto_20211101_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alexadashcams.product'),
        ),
    ]
