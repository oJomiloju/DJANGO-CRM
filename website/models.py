from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Record(models.Model):
    class_name = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    classroom = models.CharField(max_length=50)
    days = models.CharField(max_length=50)  # e.g., "Monday, Wednesday, Friday"
    start_time = models.TimeField()
    end_time = models.TimeField()
    credits = models.DecimalField(max_digits=3, decimal_places=1)
    semester = models.CharField(max_length=20)  # e.g., "Fall 2024"
    description = models.TextField(blank=True)  # Optional field for additional information

    def __str__(self):
        return f"{self.class_name} - {self.professor}"

# You can also add a method to display the class schedule
    def schedule(self):
        return f"{self.days} from {self.start_time} to {self.end_time}"