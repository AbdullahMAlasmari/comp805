from django.test import TestCase
from .modelsimport Resume
# Create your tests here.
class ResumeTestCases(TestCase):

    def setup(self):
        """
        this runs at the begging of
        """
        my_resume = Resume(first_name='Abdullah', last_name='Alasmari')
        my_resume.save()

    def test_last_name_first(self):
        r = Resume.objects.first()
        self.assertEqual(r.test_last_name_first(), Abdullah Alasmari)

from datetime import date
from django.test import TestCase

from .models import Education, Experience, Resume

class ResumeTest(TestCase):
    my_resume = Resume(first_name="Abdullah", last_name="Alasmari")
    education = Education(institution_name = "UNH", location = "NH",
        degree = "MS", major = "IT", gpa = 3.22)
    experience = Experience(title = "BTC", location = "Jeddah",
        start_date = date.today(), end_date = date.today(),
        description = "BTC at Jeddah")

    def setUp(self):
        self.resume.save()
        self.education.save()
        self.experience.save()

    def test_get_full_name(self):
        """
        Tests get_full_name method of Resume model class
        """
        self.assertEqual(self.resume.get_full_name(), "Abdullah Alasmari")

    def test_get_last_name_first_name(self):
        """
        Tests get_last_name_first_name method of Resume model class
        """
        self.assertEqual(self.resume.get_last_name_first_name(),
            "Alasmari, Abdullah")

    def test_get_experience(self):
        """
        Tests get_experience method of Resume model class
        """
        self.assertEqual(self.resume.get_experience().first(),
            self.experience)

    def test_get_education(self):
        """
        Tests get_education method of Resume model class
        """
self.assertEqual(self.resume.get_education().first(), self.education)
