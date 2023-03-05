# Generated by Django 4.1.5 on 2023-03-05 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("registrar_app", "0001_initial"),
        ("accounts_app", "0004_alter_registrar_applications"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registrar",
            name="Applications",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to="registrar_app.application",
            ),
        ),
    ]
