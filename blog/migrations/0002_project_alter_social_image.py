# Generated by Django 4.1.2 on 2022-11-03 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='social',
            name='image',
            field=models.URLField(),
        ),
    ]
