# Generated by Django 4.1.7 on 2023-04-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_login_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='status',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]