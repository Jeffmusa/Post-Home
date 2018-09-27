from django.db import models

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']

class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def __str__(self):
        return self.category_name


class Location(models.Model):
    name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length =30,null=True)
    description = models.TextField(null=True)
    location = models.ForeignKey(Location, null=True)
    category = models.ForeignKey(Category, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')
       
