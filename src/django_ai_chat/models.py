from django.db import models


class AppVar(models.Model):
    key = models.CharField(max_length=300, unique=True)
    value = models.TextField(blank=True)


class Model(models.Model):
    title = models.CharField(max_length=300, unique=True)
    name = models.CharField(max_length=300)
    system_prompt = models.TextField(blank=True)
    temperature = models.FloatField(default=1)


class Chat(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)


class Message(models.Model):
    update_time = models.DateTimeField(auto_now=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
