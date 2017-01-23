from django.conf.urls import url
from stuff.views import (
    stuff_list,
    stuff_create,
    stuff_update,
    stuff_detail,
    stuff_delete,
)

urlpatterns = [
    url(r'^$', stuff_list, name="list"),
    url(r'^create/$', stuff_create, name="create"),
    url(r'^(?P<id>\d+)/edit/$', stuff_update, name="update"),
    url(r'^(?P<id>\d+)/$', stuff_detail, name="detail"),
    url(r'^(?P<id>\d+)/delete/', stuff_delete, name="delete"),
]