from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', null=True)
    summary = models.CharField(max_length=200, blank=True)
    view = models.URLField(blank=True)
    code = models.URLField(blank=True)

    def __str__(self):
        return self.summary
