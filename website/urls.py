from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from albums.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('albums/', include('albums.urls')),
    path('admin-panel/', include('admin_panel.urls')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
