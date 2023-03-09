from user_auth.views import index,login, logout, signup
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('dashboard',login,name='dashboard'),
    path('logout',logout,name='logout'),
    path('signup',signup,name='signup'),
    path('', include('django_sso.sso_service.urls'))
]
