# Generated by Django 4.2.16 on 2024-09-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='Static/media/profile_pics/default.jpeg', upload_to='profile_pics'),
        ),
    ]
