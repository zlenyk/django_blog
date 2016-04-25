from django.conf.urls import url
from aiwars import views

urlpatterns = [
	url(r'^select/', views.selectGame),
	url(r'^(?P<id>\d+)/$', view=views.game, name='game'),

]
