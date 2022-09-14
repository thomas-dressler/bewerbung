from django.db import models

#model for skills

class Skill(models.Model):
    name = models.CharField(max_length=255)
    logo = models.URLField()
    skillLevel = models.IntegerField()
    startDate = models.DateTimeField()
    shortDescription = models.TextField()
    langOrFw = models.BooleanField()
