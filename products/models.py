from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField()
    image = models.ImageField(upload_to='images/products')
    icon = models.ImageField(upload_to='images/icon')
    body = models.TextField(max_length=500)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]


