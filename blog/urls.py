from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^classified/', views.classified),
    url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$', view=views.post, name='post'),
]
