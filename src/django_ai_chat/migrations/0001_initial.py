# Generated by Django 4.2.4 on 2023-08-29 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('system_prompt', models.TextField(blank=True)),
                ('temperature', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_ai_chat.chat')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_ai_chat.model'),
        ),
    ]
