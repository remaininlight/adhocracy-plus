# Generated by Django 2.2.4 on 2019-08-22 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_news', '0005_remove_newspage_image_and_caption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspage',
            old_name='custom_image',
            new_name='image',
        ),
    ]