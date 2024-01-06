from django.db import models

# This is a URL shortner Model
class URLShortener(models.Model):
    long_url = models.URLField(max_length=2000)  
    short_url = models.CharField(max_length=20, unique=True, db_index=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    no_of_count = models.IntegerField(default=0)

    def __str__(self):
        return self.short_url 