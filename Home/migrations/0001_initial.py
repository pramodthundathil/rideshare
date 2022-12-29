# Generated by Django 3.2.14 on 2022-12-28 03:17

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
            name='UserDetails',
            fields=[
                ('DetailID', models.AutoField(primary_key=True, serialize=False)),
                ('Phone', models.IntegerField()),
                ('House', models.CharField(max_length=255)),
                ('Location', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=255)),
                ('Contry', models.CharField(max_length=255)),
                ('PostalCode', models.CharField(max_length=255)),
                ('Document', models.FileField(upload_to='user_documents')),
                ('Message', models.CharField(max_length=255)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]