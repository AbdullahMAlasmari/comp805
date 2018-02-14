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
