from django.db import models

# Create your models here.
class Urls(models.Model):
    short_url = models.CharField(max_length=12)
    long_url = models.CharField(max_length=512)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        # managed = False
        db_table = 'urls'