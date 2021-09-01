from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('latest/',lastest, name='latest'),
    # path('', HomeView.as_view(), name='home'),
    # path('article/<slug>',ArticleDetailView.as_view(),name='article_detail'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
]
