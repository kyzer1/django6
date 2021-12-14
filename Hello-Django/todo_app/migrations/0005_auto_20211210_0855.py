# Generated by Django 3.2.9 on 2021-12-10 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_todo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='users')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todo_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ManyToManyField(null=True, to='todo_app.Category'),
        ),
    ]