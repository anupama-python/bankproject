from django.urls import path
from.import views

app_name='bankapp'
urlpatterns = [
    path('',views.base,name="base"),
    path('login', views.login, name='login'),
    path('register',views.register,name='register'),
    path('form',views.form,name='form'),
    path('new',views.new,name='new'),
    path('message',views.message,name='message'),
    path('getdata',views.getdata,name='getdata'),


]
