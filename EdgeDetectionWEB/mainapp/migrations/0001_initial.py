# Generated by Django 3.2.4 on 2021-07-27 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('titla', models.CharField(max_length=50)),
            ],
        ),
    ]
