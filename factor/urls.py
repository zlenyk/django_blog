from django.conf.urls import url
from factor import views

urlpatterns = [
    url(r'$', views.factor)
]
