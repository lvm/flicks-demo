"""flicks URL Configuration

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
from django.contrib import admin
from django.conf.urls import (
    url,
    static,
    include,
)
from rest_framework import routers
from api.api_views import (
    UserCreateView,
    FilmViewSet,
    PersonViewSet,
)

router = routers.DefaultRouter()
# public views
router.register(r'film', FilmViewSet)
router.register(r'person', PersonViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/user(/)?$', UserCreateView.as_view(), name='user-create'),
]
