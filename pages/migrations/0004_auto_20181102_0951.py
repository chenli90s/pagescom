# Generated by Django 2.1 on 2018-11-02 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_message_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='已读',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='price',
            name='已读',
            field=models.BooleanField(default=False),
        ),
    ]
