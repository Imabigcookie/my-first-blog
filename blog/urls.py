from django.urls import  re_path, path, include
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
    
]
