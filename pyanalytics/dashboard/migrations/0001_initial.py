# Generated by Django 2.0.1 on 2018-02-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('viewId', models.IntegerField(help_text='Enter the View ID for your analytics website')),
            ],
        ),
    ]