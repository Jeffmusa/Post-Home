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



class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Kenya= Location(name = 'Kenya')


# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya,Location))


    def test_save_method(self):
        self.Kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)



class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Img= Image(name = 'Jeff', description='Made with love')


# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Img,Image))

    def test_save_method(self):
        self.Img.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


   


def test_get_images_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        images_by_date = Image.days_image(date)
        self.assertTrue(len(images_by_date) == 0)


def test_get_images_today(self):
        today_images = Image.todays_images()
        self.assertTrue(len(today_images)>0)



class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Fun= Category(category_name = 'Fun')


# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Fun,Category))


    def test_save_method(self):
        self.Fun.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

