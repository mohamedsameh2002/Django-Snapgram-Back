# Generated by Django 5.0.2 on 2024-03-05 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_created_at_post_fans_alter_post_publisher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
