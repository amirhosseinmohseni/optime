# Generated by Django 4.2.2 on 2023-06-24 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_courier'),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.courier'),
        ),
    ]
