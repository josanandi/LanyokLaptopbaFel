from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contact/$', views.contact_new, name='contact_new'),
    url(r'^contactsent/$', views.contact_sent, name='contact_sent'),
    url(r'^contact/mentorsandsupporters/$', views.mentorsandsupporters, name='mentorsandsupporters'),
]
