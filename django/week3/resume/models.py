from django.db import models

# Create your models here.
class Resume(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def test_last_name_first(self):
        return "{} {}".format(self.last_name, self.first_name)
        
class Experience(models.Model):
    title = models.CharField(max_length=100,null=False, blank=False)
    location = models.CharField(max_length=100,null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    institution_name = models.CharField(max_length=100,null=False, blank=False)
    location = models.CharField(max_length=100,null=False, blank=False)
    degree = models.CharField(max_length=20,null=False, blank=False)
    major = models.CharField(max_length=100,null=False, blank=False)
    gpa = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.degree
