# Generated by Django 4.2.16 on 2024-09-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_user_uploaded_at_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
    ]
