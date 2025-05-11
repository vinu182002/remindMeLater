from django.urls import path, include
from .views import ReminderCreateView, dashboard
from . import views


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/reminders/create/', ReminderCreateView.as_view(), name='create-reminder'),
]
