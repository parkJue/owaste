# Generated by Django 4.1.3 on 2022-11-16 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('start', models.DateField(blank=True, null=True)),
                ('finish', models.DateField(blank=True, null=True)),
                ('img', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('nick', models.CharField(max_length=200)),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('facility', models.CharField(blank=True, max_length=300, null=True)),
                ('mon', models.CharField(blank=True, max_length=20, null=True)),
                ('tue', models.CharField(blank=True, max_length=20, null=True)),
                ('wed', models.CharField(blank=True, max_length=20, null=True)),
                ('thu', models.CharField(blank=True, max_length=20, null=True)),
                ('fri', models.CharField(blank=True, max_length=20, null=True)),
                ('sat', models.CharField(blank=True, max_length=20, null=True)),
                ('sun', models.CharField(blank=True, max_length=20, null=True)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('page1', models.CharField(blank=True, max_length=200, null=True)),
                ('page2', models.CharField(blank=True, max_length=200, null=True)),
                ('page3', models.CharField(blank=True, max_length=200, null=True)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
                ('tag', models.CharField(blank=True, max_length=400, null=True)),
                ('region', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('lat', models.CharField(blank=True, max_length=20, null=True)),
                ('lon', models.CharField(blank=True, max_length=20, null=True)),
                ('img', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Oreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(default='owaste', max_length=10)),
                ('content', models.TextField()),
                ('register_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zerowaste.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Nkreview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('reg_date', models.DateField()),
                ('nick', models.CharField(max_length=200)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zerowaste.shop')),
            ],
        ),
    ]
