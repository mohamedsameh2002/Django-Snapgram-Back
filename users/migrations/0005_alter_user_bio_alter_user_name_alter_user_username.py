# Generated by Django 5.0.2 on 2024-03-06 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=15, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=10, unique=True, verbose_name='Username'),
        ),
    ]