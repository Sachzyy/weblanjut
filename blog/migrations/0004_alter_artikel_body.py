# Generated by Django 3.2.7 on 2021-11-09 09:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_artikel_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
