# Generated by Django 3.2.14 on 2023-03-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_rename_messages_usermessages'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='Country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='Contry',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
