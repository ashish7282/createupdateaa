# Generated by Django 4.2.1 on 2023-06-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user1_delete_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user1',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='user1',
            name='bio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user1',
            name='propic',
            field=models.ImageField(max_length=255, upload_to='pictures/'),
        ),
    ]