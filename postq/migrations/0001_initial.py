# Generated by Django 4.1.4 on 2022-12-12 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('adress', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('position', models.CharField(max_length=20)),
                ('salary', models.IntegerField(null=True)),
                ('work_experience', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VIPClient',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='postq.client')),
                ('vip_status_start', models.DateField(null=True)),
                ('donation_amount', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('postq.client',),
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=16)),
                ('id_card', models.CharField(max_length=10)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passports', to='postq.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postq.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postq.workproject')),
            ],
        ),
    ]