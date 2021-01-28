from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_dashboard, name="dashboard"),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('article/<int:id>', views.articles, name='article-edit'),
    path('article', views.articles, name='article'),
    path('article-approval', views.article_approval, name='article-approval'),
    path('article-edited', views.article_edited, name='article-edited'),
    path('approve/<int:id>', views.approve_article, name='approve'),
    path('reject/<int:id>', views.reject_article, name='reject'),
]