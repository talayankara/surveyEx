# Generated by Django 2.1.7 on 2019-02-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyExample', '0002_auto_20190223_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyoption',
            name='option_text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyoption',
            name='option_type',
            field=models.CharField(default='Text', max_length=20),
        ),
    ]