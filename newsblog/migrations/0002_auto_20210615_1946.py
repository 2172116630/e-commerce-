# Generated by Django 3.2.4 on 2021-06-15 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsblog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
