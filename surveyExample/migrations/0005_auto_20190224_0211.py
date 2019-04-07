# Generated by Django 2.1.7 on 2019-02-23 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveyExample', '0004_auto_20190224_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='survive_id',
            new_name='survey_id',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='survey_id',
        ),
        migrations.RemoveField(
            model_name='surveyoption',
            name='deneme',
        ),
        migrations.AddField(
            model_name='surveyoption',
            name='question',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='surveyExample.Surveyquestion'),
            preserve_default=False,
        ),
    ]