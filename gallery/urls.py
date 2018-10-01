from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    
    url('^today/$',views.uploads,name='uploadsToday'),
    # url(r'^history/(\d{4}-\d{2}-\d{2})/$',views.past_uploads,name = 'pastUploads'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^$',views.all,name = 'all'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^location/(\w+)',views.locations,name='location'),
    url(r'^category/(\w+)',views.category,name='category'),

]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
