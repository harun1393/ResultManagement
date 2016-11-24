"""resultmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
import login.views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^result/',include('results.urls')),
    url(r'^teacher/',include('teachers.urls')),
    url(r'^students/',include('students.urls')),
    url(r'^subjects/',include('subjects.urls')),
    url(r'^login/',login.views.user_login,name='login'),
    url(r'^logout/',login.views.user_logout,name='logout'),
]
