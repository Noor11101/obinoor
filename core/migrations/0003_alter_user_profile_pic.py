# Generated by Django 4.2.16 on 2024-09-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics'),
        ),
    ]
