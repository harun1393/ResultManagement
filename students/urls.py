from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_students, name='students-list'),
    url(r'^add-student$', views.add_students, name='add-students'),
]