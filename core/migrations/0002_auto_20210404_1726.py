# Generated by Django 3.1.7 on 2021-04-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="new",
            name="source",
            field=models.CharField(
                choices=[("MR", "MARCA"), ("MC", "MOI CELESTE"), ("VG", "LA VOZ DE GALICIA"), ("FV", "FARO DE VIGO")],
                max_length=2,
            ),
        ),
    ]
