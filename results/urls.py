from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.results, name='results'),
    url(r'^add-result/', views.add_result, name='add-result'),
    #url(r'^add-marks/', views.add_marks, name='add-marks'),
    #url(r'^all-exams/', views.all_exams, name='all-exams'),
    #url(r'^generate-result/', views.generate_result, name='generate-result'),
]