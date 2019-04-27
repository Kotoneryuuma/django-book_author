from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.add),
    url(r'^shows/process$', views.add_process),
    url(r'^edit/(?P<idr>\d+)/process$', views.edit_process),
    url(r'^shows/(?P<idr>\d+)/delete$', views.delete),
    url(r'^shows/(?P<idr>\d+)$', views.show),
    url(r'^shows/(?P<idr>\d+)/edit$', views.edit),
]