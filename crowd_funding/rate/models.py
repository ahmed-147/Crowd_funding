from django.db import models
from project.models import Project
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
#rates (id (pk), rate [1-5], user_id (fk), project_id (fk) )

class Rate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'user name: {self.user} rate: {self.rate} project: {self.project}'
