# Generated by Django 5.0.3 on 2024-03-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='cvimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_images', models.ImageField(upload_to='cimg')),
            ],
        ),
    ]