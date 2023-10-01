"""
URL configuration for QuestionBox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from django.contrib.auth.views import LoginView, LogoutView
from faq_api.views import QuestionViewSet


from . import views

router = routers.DefaultRouter()
router.register(r"questions", QuestionViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("faq.urls")),
    path("faq/api/v1/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("accounts/register/", views.register, name="register"),
]

if settings.DEBUG:
    # do not do this in prod
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
