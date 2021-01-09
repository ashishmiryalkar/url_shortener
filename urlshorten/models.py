from django.db import models


class URLShortener(models.Model):
    short_url = models.CharField(max_length=10)
    actual_url = models.CharField(max_length=200)
    clicks_count = models.IntegerField(default=0)

    def __str__(self):
        return self.short_url