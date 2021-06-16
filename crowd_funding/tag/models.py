from django.db import models
from django.conf import settings
from project.models import Project
# Create your models here.
class Tag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name




class proiect_tag(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,
                            on_delete=models.CASCADE)

    def __str__(self):
        return f'project: {self.project.title} tag: {self.tag.name}'
