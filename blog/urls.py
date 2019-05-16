from . import views
from django.urls import path, re_path
from django.urls import include


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    re_path(r'^tinymce/', include('tinymce.urls')),
] 
