# Generated by Django 3.2.16 on 2023-05-10 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('id',)},
        ),
    ]