# Generated by Django 3.0.7 on 2020-07-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUTH', '0004_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default="{% static 'img/profile.png' %}", upload_to=''),
        ),
    ]
