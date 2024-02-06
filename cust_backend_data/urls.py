
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from cust_backend_app.views import success_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('cust_backend_app.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('success/', success_view, name='success'),
]


