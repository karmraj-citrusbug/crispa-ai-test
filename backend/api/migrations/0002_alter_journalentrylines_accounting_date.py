# Generated by Django 3.2.24 on 2024-02-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentrylines',
            name='accounting_date',
            field=models.DateField(),
        ),
    ]
