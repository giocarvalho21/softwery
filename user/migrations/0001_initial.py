# Generated by Django 3.1.4 on 2020-12-31 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('login', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('profilePhoto', models.ImageField(blank=True, null=True, upload_to='profilePhotos')),
                ('dateBirth', models.DateField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='company.company')),
                ('menus', models.ManyToManyField(db_table='SFT_USER_MENU', to='menu.Menu')),
            ],
            options={
                'db_table': 'SFT_USER',
            },
        ),
    ]
