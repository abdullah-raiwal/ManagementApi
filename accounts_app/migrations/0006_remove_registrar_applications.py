# Generated by Django 4.1.5 on 2023-03-05 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts_app", "0005_alter_registrar_applications"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registrar",
            name="Applications",
        ),
    ]
