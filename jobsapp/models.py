from django.db import models
from django.shortcuts import reverse


# Create your models here.
class AddJobs(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    skills_required = models.TextField()
    education = models.CharField(max_length=50)
    experience = models.CharField(max_length=20, blank=True)
    employment_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title


class ApplyJob(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details_of_job', kwargs={'pk': self.pk})
