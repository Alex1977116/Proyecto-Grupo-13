# Generated by Django 3.1.7 on 2021-06-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_quiz_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='number_of_questions',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='quiz',
            name='time',
            field=models.IntegerField(default='1', help_text='Duración del cuestionario en segundos'),
        ),
    ]
