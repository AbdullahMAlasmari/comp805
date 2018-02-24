from django.test import TestCase
from .models import Education, Experience, Resume

class ResumeTestCase(TestCase):
    #declare instance variables.
    my_resume = None
    my_experience = None
    my_education = None

    def setUp(self):
        self.my_resume = Resume.objects.create (first_name="Abdullah",
        last_name="Alasmari")
        self.my_education = Education.objects.create(
            parent_resume=self.my_resume,
            institution_name = "UNH",
            location = "NH",
             major = "IT",
            degree = "MS",
            gpa = 3.22
            )
        self.my_experience = Experience.objects.create(
            parent_resume=self.my_resume,
            title = "Research Assistant",
            location = "Boston",
            start_date = 2016-6-10,
            end_date = 2016-8-11,
            description = "Help in labs"
                )

    def test_starting_conditions(self):
        """
        Check if education, Resume, and Experiencec instance existself.
        """
        self.assertIsInstance(self.my_resume, Resume)
        self.assertIsInstance(self.my_education, Education)
        self.assertIsInstance(self.my_experience, Experience)

    def test_get_full_name(self):
        """
        Tests get_full_name method of Resume model class
        """
        self.assertEqual("Abdullah Alasmari",
        self.my_resume.get_full_name())

    def test_last_name_first_name(self):
        """
        Tests get_last_name_first_name method of Resume model class
        """
        self.assertEqual("Alasmari Abdullah",
        self.my_resume.get_last_name_first_name())

    def test_get_experience(self):
        """
        Tests get_experience method of Resume model class
        """
        self.assertEqual(list(self.my_resume.get_experience()),
        list(self.my_resume.experience_set.all()))

    def test_get_education(self):
        """
        Tests get_education method of Resume model class
        """
        self.assertEqual(list(self.my_resume.get_education()),
        list(self.my_resume.education_set.all()))
