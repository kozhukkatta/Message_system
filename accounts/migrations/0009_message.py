# Generated by Django 4.1.5 on 2023-03-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_login_id_alter_login_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('mid', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=10)),
                ('option', models.CharField(blank=True, max_length=10)),
                ('message', models.CharField(blank=True, max_length=5000)),
            ],
        ),
    ]
