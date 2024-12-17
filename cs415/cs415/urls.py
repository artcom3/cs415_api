"""
URL configuration for cs415 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from cs415.views import UserphoneAPIView, WebUserAPIView, AddresstypeAPIView, PagedataAPIView, PhonetypeAPIView, UseraddressAPIView, UserinfoAPIView
from cs415.views import SingleWebUserAPIView, SingleAddresstypeAPIView, SinglePagedataAPIView, SinglePhonetypeAPIView, SingleUseraddressAPIView, SingleUserinfoAPIView, SingleUserphoneAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# for swagger documentation
schema_view = get_schema_view(
   openapi.Info(
      title="cs415 REST API Endpoints",
      default_version='1.0',
      description="API Documentation for cs415 Website API Project",
   ),
   public=True,
)

urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('users', WebUserAPIView.as_view()),
    path('users/<int:web_user_id>', SingleWebUserAPIView.as_view()),
    path('address-types', AddresstypeAPIView.as_view()),
    path('address-types/<int:address_type_id>', SingleAddresstypeAPIView.as_view()),
    path('addresses', UseraddressAPIView.as_view()),
    path('addresses/<int:user_address_id>', SingleUseraddressAPIView.as_view()),
    path('phone-types', PhonetypeAPIView.as_view()),
    path('phone-types/<int:phone_type_id>', SinglePhonetypeAPIView.as_view()),
    path('phones', UserphoneAPIView.as_view()),
    path('phones/<int:user_phone_id>', SingleUserphoneAPIView.as_view()),
    path('user-infos', UserinfoAPIView.as_view()),
    path('user-infos/<int:user_info_id>', SingleUserinfoAPIView.as_view()),
    path('pages', PagedataAPIView.as_view()),
    path('pages/<int:page_id>', SinglePagedataAPIView.as_view()),
]