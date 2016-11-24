from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^my-subjects$', views.my_subjects, name='my-subjects'),
    url(r'^all/', views.all_subjects, name='all-subjects'),
]