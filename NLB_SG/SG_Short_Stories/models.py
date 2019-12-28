from django.db import models

#step 1 make models for data
class Book(models.Model):
    title =models.CharField(max_length=100)
    author =models.CharField(max_length=100)
    language =models.CharField(max_length=30, blank=True)
    summary = models.TextField()
    publish_year = models.DateField()
    download_link = models.URLField()

    
