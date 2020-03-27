from django.db import models

# Create your models here.

class Signup(models.Model):
    email = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email+' | '+str(self.timestamp)
