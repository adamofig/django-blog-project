"""blogtoy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from blog.views import welcome, articles, login_user, article_approval, logout_user, approve_article, articles_edited, reject_article

urlpatterns = [
    path('', welcome),
    path('login', login_user),
    path('logout', logout_user),
    path('blog', include('blog.urls')),
    path('article/<int:id>', articles),
    path('article', articles),
    path('article-approval', article_approval),
    path('articles-edited', articles_edited),
    path('approve/<int:id>', approve_article),
    path('reject/<int:id>', reject_article),
    path('admin/', admin.site.urls),
]
