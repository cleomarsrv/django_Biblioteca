# Generated by Django 4.2 on 2023-05-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0012_alter_livrofisico_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='dataMorte',
            field=models.DateField(blank=True, null=True, verbose_name='Morte'),
        ),
    ]
