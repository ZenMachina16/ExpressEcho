
from django.urls import path  # Import include function

from .views import UserRegisterView, UserEditView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='password_change'),
    # path('password_success', views.password_success, name='password_success'),
    
    # Add the following line to match user IDs and include 'members.urls'
    # path('<int:uid>/', include('members.urls')),
        ]


