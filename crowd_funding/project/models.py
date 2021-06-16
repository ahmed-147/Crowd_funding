from django.db import models

from category.models import Category
from django.conf import settings


# Create your models here.
# projects (id (pk), title, details, target, currnt_donation, start_date, end_date, avg_rate, categ_id (fk)
# , user_id (fk) )
class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    details = models.TextField()
    target = models.FloatField(default=0)
    current_donation = models.FloatField(default=0)
    start_date = models.DateField(auto_now=False, auto_now_add=False, )
    end_date = models.DateField(auto_now=False, auto_now_add=False, )
    sum_rate = models.FloatField(default=0)
    count_rated_user = models.IntegerField(default=0)
    avg_rate = models.FloatField(default=0)
    report_count = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

    def count_avg_rate(self):
        if self.count_rated_user == 0:
            return "No user rated this project"
        self.avg_rate = self.sum_rate / self.count_rated_user
        return self.sum_rate / self.count_rated_user

    def __str__(self):
        return "Project title: " + self.title + " |user name: " + self.user.username + " " + self.title + " |category: " + self.category.name

    def first_img(self):
        project = Project.objects.filter(pk=self.pk).first()
        img = Project_imgs.objects.filter(project=project).first()
        return img
    def all_imgs(self):
        project = Project.objects.filter(pk=self.pk).first()
        imgs = Project_imgs.objects.filter(project=project)
        return imgs


class Project_imgs(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)
    img = models.ImageField(upload_to='projects_pictures/')

    def __str__(self):
        return "Images: " + self.img.url + " project: " + self.project.title
