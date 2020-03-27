
from django.urls import path
from . import views
from .views import index, blog,post,search

urlpatterns = [
                  path('', index, name='home'),
                  path('blog/', blog, name='blog'),
                  path('post/<id>/', post, name='post'),
                  path('search/', search, name='search'),
                  # path('<int:post_id>/', views.detail, name='detail'), #this is optional

              ]


