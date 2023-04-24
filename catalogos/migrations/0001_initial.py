# Generated by Django 4.2 on 2023-04-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field_name', models.CharField(help_text='Enter field documentation', max_length=20, verbose_name='teste_field_name')),
            ],
            options={
                'ordering': ['-my_field_name'],
            },
        ),
    ]
