# Generated by Django 4.2 on 2023-05-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0004_rename_datamorte_autor_datamorte_alter_livro_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livrofisico',
            old_name='imprimir',
            new_name='publicacao',
        ),
    ]