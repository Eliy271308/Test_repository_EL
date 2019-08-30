# Generated by Django 2.2.4 on 2019-08-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите имя', max_length=150)),
                ('last_name', models.CharField(help_text='Введите фамилию', max_length=150)),
                ('date_birthday', models.DateField(blank=True, help_text='Введите дату рождения', null=True)),
                ('country', models.CharField(help_text='Введите страну рождения', max_length=150)),
            ],
        ),
    ]