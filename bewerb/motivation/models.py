from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

#model for motivation

class Motivation(models.Model):
    headline = models.CharField(max_length=255, blank=False)
    jobPosition = models.CharField(max_length=255, blank=False)
    motivationText = models.TextField()
    assignedTo = models.CharField(max_length=255, blank=True)
    assignedUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
