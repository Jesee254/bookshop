# Generated by Django 4.2.7 on 2024-01-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books_tbl',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='books_tbl',
            name='ISBN',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='books_tbl',
            name='authors',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='books_tbl',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
