from django.db import models

# Create your models here.
class Crime(models.Model):
    crime_type = models.CharField(max_length=100)  # Type of crime (e.g., theft, cybercrime)
    location = models.CharField(max_length=100)    # Location of the crime
    date = models.DateField()                      # Date of the crime
    description = models.TextField()               # Description of the crime
    severity = models.IntegerField()               # Severity level (e.g., 1-10)

    def __str__(self):
        return f"{self.crime_type} at {self.location} on {self.date}"