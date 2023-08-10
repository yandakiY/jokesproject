from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Category(models.Model):
    
    libelle = models.CharField(max_length=180)
    view = models.BooleanField(default=True)
    
    def __str__(self):
        return self.libelle
    

class Joke(models.Model):
    
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=150)
    date_pub = models.DateTimeField("Date pub")
    view = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.question
    
    def is_recent(self):
        time = timezone.now()
        return time - datetime.timedelta(days=1) <= self.date_pub <= time
