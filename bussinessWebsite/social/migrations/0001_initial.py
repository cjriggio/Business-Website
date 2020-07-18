# Generated by Django 3.0.7 on 2020-07-12 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Key name')),
                ('name', models.CharField(max_length=200, verbose_name='Social Networks')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Link')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date of last modification')),
            ],
            options={
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
                'ordering': ['name'],
            },
        ),
    ]