from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home',views.HomeView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('loginpage/',views.LoginView.as_view(),name='loginpage'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('register/',views.RegView.as_view(), name='register'),
    path('table/',views.orderView,name='table'),
      path('',views.navbarView.as_view(), name='navbarView'),

    

]