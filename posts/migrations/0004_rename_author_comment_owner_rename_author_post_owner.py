# Generated by Django 4.0.4 on 2022-05-24 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_authorid_comment_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='owner',
        ),
    ]