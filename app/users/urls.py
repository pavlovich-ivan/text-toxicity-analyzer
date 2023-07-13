from django.urls import path, include
from .views import RegisterView, ChangePasswordView, ProfileView, EditPersonalDataView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('edit_personal_data/', EditPersonalDataView.as_view(), name="edit_personal_data"),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]