# Generated by Django 3.2.5 on 2021-09-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_organization_files_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization_files',
            name='folder',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
