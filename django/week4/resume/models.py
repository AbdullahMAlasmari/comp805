from django.db import models

# Create your models here.
class Resume(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def test_last_name_first(self):
        return "{} {}".format(self.last_name, self.first_name)

    def get_full_name(self):
        """
        returns full name "Firstname Lastname"
        """
        return "{} {}".format(self.first_name, self.last_name)

    def get_education(self):
        """
        returns all foreign key related "Education" objects
        """
        return self.education_set.all()

    def get_experience(self):
        """
        returns all foreign key related "Experience" objects
        """
        return self.experience_set.all()


class Experience(models.Model):
    parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100,null=False, blank=False)
    location = models.CharField(max_length=100,null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
    institution_name = models.CharField(max_length=100,null=False, blank=False)
    location = models.CharField(max_length=100,null=False, blank=False)
    degree = models.CharField(max_length=20,null=False, blank=False)
    major = models.CharField(max_length=100,null=False, blank=False)
    gpa = models.FloatField(null=False, blank=False)

    def __str__(self):
        return" {}, {}, {},{}, {}".format(self.institution_name, self.location, self.degree, self.major, self.gpa)
