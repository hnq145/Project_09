# Generated by Django 5.1.5 on 2025-02-04 16:21

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
