# Generated by Django 4.2.1 on 2023-05-25 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]
