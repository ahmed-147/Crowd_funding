from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#profiles (id (pk), title, user_id (fk) (1:1), imgs, phone, email, birth_date, facebook_link, country )
class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    phone = models.CharField(max_length=11, blank=True)
    img = models.ImageField()
    birth_date = models.DateField(null=True, blank=True)
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'user name: {self.user} telephone number: {self.phone}'
    
    
