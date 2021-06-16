from django.db import models

from django.conf import settings
from project.models import Project
# Create your models here.
#comments (id (pk), text, user_id (fk) , project_id (fk) )

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    text = models.TextField()
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)
    Publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user name: {self.user} project: {self.project} comment: {self.text} date: {self.Publish_date}'
