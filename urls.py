
from django.contrib import admin
from django.urls import path
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Sign_up,name='signup'),
    path('login/', views.User_login,name='login'),
    path('profile/', views.User_profile,name='profile'),
    path('logout/', views.User_logout,name='logout'),
    path('changepass/', views.User_change,name='changepass'),
]
