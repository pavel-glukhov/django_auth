# Generated by Django 4.0.5 on 2022-06-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_options_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
