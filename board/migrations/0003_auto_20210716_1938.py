# Generated by Django 3.2.4 on 2021-07-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Board',
            new_name='boad_type',
        ),
        migrations.AlterField(
            model_name='board',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
