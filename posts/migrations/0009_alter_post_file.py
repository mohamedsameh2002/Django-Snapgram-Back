# Generated by Django 5.0.2 on 2024-03-11 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='posts_files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'jpg', 'png', 'svg'])]),
        ),
    ]