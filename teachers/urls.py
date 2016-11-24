from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.admin_panel, name='admin-panel'),
    url(r'classes/',views.class_management, name='classes'),
    url(r'add-teacher$',views.add_teacher, name='add-teacher'),
    url(r'teachers-list$',views.teachers_list, name='teachers-list'),

]