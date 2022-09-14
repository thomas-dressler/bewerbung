from django.db import models

#model for curriculum vitae

class Cv(models.Model):
    position = models.CharField(max_length=255)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    descriptionText = models.TextField()
    location = models.CharField(max_length=255, blank=False)
    organisationName = models.CharField(max_length=255, blank=False)
