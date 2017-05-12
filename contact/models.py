from django.db import models

class Contact(models.Model):
    subject = models.CharField(max_length=500, blank=True)
    content = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.content
# Create your models here.
