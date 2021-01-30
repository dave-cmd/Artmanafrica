from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image



# Create your models here.
class Post(models.Model):
    title1 = models.CharField(max_length=100, null=True)
    title2 = models.CharField(max_length=100, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    art = models.ImageField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
   

    def __str__(self):
        return f"Post {self.timestamp}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def save(self):
        super().save()

        img = Image.open(self.art.path)
        output_size = (800, 600)
        img.thumbnail(output_size)
        img.save(self.art.path)
        print("~~~~~~~Resized~~~~~~~")




    
