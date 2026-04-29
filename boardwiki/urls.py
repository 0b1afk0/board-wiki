"""
URL configuration for boardwiki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from games.views import g_list, g_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', g_list, name='g_list'),
    path('g/<int:game_id>/', g_detail, name='g_detail'),
] + static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'templates')

# Перехват всех остальных запросов для показа кастомной страницы 404 даже при DEBUG=True
from django.urls import re_path
from games.views import page_not_found

urlpatterns += [
    re_path(r'^.*$', page_not_found),
]

handler404 = 'games.views.page_not_found'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
