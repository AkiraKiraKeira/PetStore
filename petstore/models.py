from django.conf import settings
from django.db import models
from django.utils import timezone


class Item(models.Model):
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    price = models.IntegerField()
    promo = models.BooleanField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def _str_(self):
        return self.title

# class Rio(models.Model):
#     company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     price = models.IntegerField()
#     promo = models.BooleanField()
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def _str_(self):
#         return self.title