# Generated by Django 4.2.3 on 2023-07-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_storage_arrears_over_provider"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storage",
            name="arrears_over_provider",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
