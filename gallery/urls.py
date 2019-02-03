from django.conf.urls import url

from . import views

app_name = 'agileProject'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_image, name='addImage'),
]
