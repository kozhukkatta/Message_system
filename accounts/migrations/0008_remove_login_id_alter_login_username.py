# Generated by Django 4.1.5 on 2023-03-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_login_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='id',
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(blank=True, max_length=10, primary_key=True, serialize=False),
        ),
    ]
