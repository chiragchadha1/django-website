from django.db import models

# Create your models here.
class Team (models.Model): # use the (models.Model) to specify that it's a sub-class of Models

    name = models.CharField(max_length=30) # defining the type of name
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} from {self.city}"