from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^html&css', views.htmlCss, name='htmlCss'),
    url(r'^javascript', views.javaScript, name='javaScript'),
    url(r'^python', views.python, name='python'),
    url(r'^php', views.php, name='php'),
    ]
