from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', MainPageView.as_view(), name='main-page'),
    path('admin/', admin.site.urls), 
    path('albums/', include('albums.urls')),
    # path('posts/', include('blog.urls')), 
    # path('signup/', SignupView.as_view(), name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('profile/<int:pk>/', UserProfile.as_view(), name='profile'),
]
