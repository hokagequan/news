from django.db import models

# Create your models here.
class News(models.Model):

    title = models.TextField()
    url = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
		