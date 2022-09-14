from django.db import models
# model for References


class Tech(models.Model):
    techName = models.CharField(max_length=255)

    def __str__(self):
        return self.techName


class Reference(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.URLField()
    techStack = models.ManyToManyField(Tech)
    organisationName = models.CharField(max_length=255, blank=False)

