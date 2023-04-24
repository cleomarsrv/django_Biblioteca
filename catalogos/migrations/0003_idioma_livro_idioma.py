# Generated by Django 4.2 on 2023-04-24 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_autor_genero_livro_livrofisico_meumodelo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='digite o idioma do livro', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='livro',
            name='idioma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogos.idioma'),
        ),
    ]