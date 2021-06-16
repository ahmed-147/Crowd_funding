from django.db import models
from django.conf import settings
from project.models import Project

# Create your models here.
#donations (id (pk), donation_val ,user_id (fk), project_id (fk))
class Donation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)
    value = models.FloatField(default=0)
    def __str__(self):
        return f'user name: {self.user} project: {self.project} donation value: {self.value}'
