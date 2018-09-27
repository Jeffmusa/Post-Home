from django.test import TestCase
from .models import Editor,Category,Location,Image

# Create your tests here.


class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Jeff= Editor(first_name = 'Jeff', last_name ='Musa', email ='jeff@moringaschool.com')


# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Jeff,Editor))

    def test_save_method(self):
        self.Jeff.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)