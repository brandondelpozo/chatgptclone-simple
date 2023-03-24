from django.db import models

class Chat(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()