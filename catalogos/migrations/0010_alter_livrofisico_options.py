# Generated by Django 4.2 on 2023-05-05 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0009_alter_livrofisico_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livrofisico',
            options={'ordering': ['dataDevolucao'], 'permissions': (('fazerDevolucao', 'definir livro como devolvido'), ('verEmprestimos', ' ver todos os emprestimos'))},
        ),
    ]