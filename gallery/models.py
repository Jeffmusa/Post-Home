from django.db import models
import datetime as dt

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()


    class Meta:
        ordering = ['first_name']

class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    


class Location(models.Model):
    name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()


class Image(models.Model):
    name = models.CharField(max_length =30,null=True)
    description = models.TextField(null=True)
    location = models.ForeignKey(Location, null=True)
    category = models.ForeignKey(Category, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    @classmethod
    def uploads(cls):
        today = dt.date.today()
        uploads = cls.objects.filter(pub_date__date = today)
        return uploads

    @classmethod
    def all_uploads(cls,date):
        uploads = cls.objects.filter(pub_date__date = date)
        return uploads

    @classmethod
    def search_by_name(cls,search_term):
        uploads = cls.objects.filter(name__icontains=search_term)
        return uploads
       
