from django.db import models
from django.conf import settings
# Create your models here.
#categories ( id (pk), categ_name )
class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

