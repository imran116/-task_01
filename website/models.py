from django.db import models

class slider_01(models.Model):
    subtitle = models.CharField(max_length=30)
    title = models.CharField(max_length=70)
    bottom_title = models.CharField(max_length=170)
    botton_text = models.CharField(max_length=170)
    bottom_url = models.CharField(max_length=170)
    phone_no = models.CharField(max_length=20)

class Services_01(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='services/')
    description = models.CharField(max_length=100)

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    project_no = models.CharField(max_length=20)
    project_dese = models.CharField(max_length=30)