from django.db import models
import datetime
# Create your models here.
class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(default="")
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)

class Testimonials(models.Model):
    Testimonial_desc = models.TextField(default="")
    name = models.CharField(max_length=100)
    position = "client"
class NewsPost(models.Model):
    dates = datetime.date.today()
    date = dates.strftime('%Y-%m-%d')
    # month = date('%B')
    # day = date('%d')

    img = models.ImageField(upload_to='pics')
    post_desc = models.TextField(default="")



