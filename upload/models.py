from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)