# Generated by Django 4.2 on 2023-05-05 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0008_alter_livrofisico_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livrofisico',
            options={'ordering': ['dataDevolucao'], 'permissions': (('fazer-devolucao', 'definir livro como devolvido'), ('ver-emprestimos', ' ver todos os emprestimos'))},
        ),
    ]