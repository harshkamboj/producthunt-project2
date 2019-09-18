from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=250)
    pub_Date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    icon =  models.ImageField(upload_to='images/')
    body = models.TextField()
    url  = models.TextField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return  self.body[:50]

    def pub_date1(self):
        return  self.pub_Date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title