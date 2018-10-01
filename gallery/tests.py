from django.test import TestCase
from .models import Editor,Category,Location,Image
import datetime as dt


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

    def test_delete(self):
        post = Editor.objects.filter(id=1)
        post.delete()
        posts = Editor.objects.all()
        self.assertTrue(len(posts)==0)

    def test_data(self):
        self.assertTrue(self.Jeff.first_name,"Jay")



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


    def test_update_location(self):
        self.Kenya.save_location()
        self.update_location = Location.objects.filter(name='Africa').update(name = 'Kenya')
        self.updated_location = Location.objects.get(name='Kenya')
        self.assertTrue(self.updated_location.name,'Kenya')


    def test_delete(self):
        location = Location.objects.filter(id=1)
        location.delete()
        area = Location.objects.all()
        self.assertTrue(len(area)==0)

    def test_get_location_by_id(self):
        self.Kenya.save()
        locale = Location.objects.get(id=1)
        self.assertTrue(locale.name,'nairobi')
    
    def test_data(self):
        self.assertTrue(self.Kenya.name,"nairobi")

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

    def test_data(self):
        self.assertTrue(self.Img.name,"test")

    def test_delete(self):
        post = Image.objects.filter(id=1)
        post.delete()
        posts = Image.objects.all()
        self.assertTrue(len(posts)==0)

    def test_get_post_by_id(self):
        self.Img.save()
        posts = Image.objects.get(id=1)
        self.assertTrue(posts.name,'kol')






class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Fun= Category(category_name = 'Fun')


# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Fun,Category))

    def test_data(self):
        self.assertTrue(self.Fun.category_name,"tpm")

    def test_save_method(self):
        self.Fun.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

    def test_delete(self):
        category = Category.objects.filter(id=1)
        category.delete()
        cat = Category.objects.all()
        self.assertTrue(len(cat)==0)


    def test_get_category_by_id(self):
        self.Fun.save()
        cat = Category.objects.get(id=1)
        self.assertTrue(cat.category_name,'test')

    # def test_update_category(self):
    #     self.Fun.save()
    #     self.update_cat = Category.objects.filter(category_name='hey').update(category_name = 'yoh')
    #     self.updated_cat = Category.objects.get(category_name='yoh')
    #     self.assertTrue(self.updated_cat.name,'yoh')

