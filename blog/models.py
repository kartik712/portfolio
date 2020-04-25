from django.db import models

class Blogs(models.Model):

    title = models.CharField(max_length=30)
    creation_date = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.title