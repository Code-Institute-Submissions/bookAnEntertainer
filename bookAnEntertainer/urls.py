"""bookAnEntertainer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from home import views as home_views
from entertainers import views as entertainer_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_views.get_index, name="home"),
    url(r'^entertainers/', entertainer_views.list_entertainers_all, name="entertainers"),
    url(r'^entertainers/(?P<post_id>[0-9]+)/$', entertainer_views.entertainer_details),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
