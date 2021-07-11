from django.urls import path
from . import views


urlpatterns= [
    path('',views.user_login,name='login'),
    path('register/',views.user_register,name='register'),
    path('post/',views.user_post,name='post')

]