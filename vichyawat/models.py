from django.db import models


class Contact(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254, default='')
    message = models.TextField()

    def __str__(self):
        return self.subject
