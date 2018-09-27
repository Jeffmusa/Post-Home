from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^welcome',views.welcome,name = 'welcome'),
    url('^$',views.uploads,name='uploadsToday'),
    url(r'^history/(\d{4}-\d{2}-\d{2})/$',views.past_uploads,name = 'pastUploads'),

]