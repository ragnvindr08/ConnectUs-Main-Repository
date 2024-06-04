# Generated by Django 4.2.11 on 2024-06-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='posts/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
