# Generated by Django 3.2.9 on 2022-03-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_alter_hf_mentoralando_alter_hf_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='git',
            options={'verbose_name': 'Git-profil', 'verbose_name_plural': 'Git-profilok'},
        ),
        migrations.AlterField(
            model_name='git',
            name='platform',
            field=models.CharField(max_length=255),
        ),
    ]