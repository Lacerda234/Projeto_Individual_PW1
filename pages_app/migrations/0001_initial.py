# Generated by Django 3.2.12 on 2022-03-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('raça', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('g', 'Gato'), ('c', 'Cachorro')], max_length=1)),
                ('sexo', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.IntegerField(max_length=16)),
                ('telefone', models.IntegerField(max_length=12)),
                ('idade', models.IntegerField(max_length=2)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sexo', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino')], max_length=1)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('profissão', models.CharField(max_length=30)),
            ],
        ),
    ]
