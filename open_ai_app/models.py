from django.db import models

# Create your models here.

class ChatTable(models.Model):
    id = models.AutoField(primary_key=True)
    prompt = models.TextField()
    output = models.TextField()

    def __str__(self):
        return self.prompt


class ImageTable(models.Model):
    id = models.AutoField(primary_key=True)
    prompt = models.TextField()
    img_url = models.TextField()

    def __str__(self):
        return self.prompt
