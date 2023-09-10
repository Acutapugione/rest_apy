from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.



class Welcome(models.Model):
    @staticmethod
    def get_greetings( *args, **kwargs):
        curr_time = now().time()
        greetings = 'Good '
        if 5 <= curr_time.hour < 12:
            greetings += " morning"
        elif 12 <= curr_time.hour < 18:
            return " day"
        elif 18 <= curr_time.hour < 23:
            return " evening"
        else:
            return " night"    
        greetings = f"{greetings}!"
        return greetings


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    
    greetings = models.CharField(
        max_length=100,
        blank=True, 
        null=False,
        default=get_greetings()
    )
    
    
    
        
class Info(models.Model):
    date = models.DateField(
        auto_now=True,
        blank=True,
        auto_now_add=False,
        
    )
    time = models.TimeField(
        auto_now=True,
        blank=True,
        auto_now_add=False,
        
    )
    weekday = models.CharField(
        max_length=100,
        blank=True,
        default=now().weekday(),
    )


class Webservise(models.Model):
    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        blank=True,
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return str(self.timestamp)
    