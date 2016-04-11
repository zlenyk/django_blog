from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^home/', TemplateView.as_view(template_name='index.html')),
    url(r'^error/', TemplateView.as_view(template_name='error.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'$', TemplateView.as_view(template_name='index.html')),
]
