from django.db import models

# Create your models here.
class Urls(models.Model):
    shortened_url = models.CharField(max_length=12)
    full_url = models.CharField(max_length=512)
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'urls'