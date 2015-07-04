from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=20)

    def __unicode__(self):
        return self.name