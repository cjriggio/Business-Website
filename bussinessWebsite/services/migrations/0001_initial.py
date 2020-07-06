# Generated by Django 3.0.7 on 2020-07-06 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtitle')),
                ('content', models.TextField(verbose_name='Content')),
                ('image', models.ImageField(upload_to='services', verbose_name='Image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date and time of creation')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date and time of last change')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
                'ordering': ['-created'],
            },
        ),
    ]
