from django.urls import path
import accounts.views

urlpatterns = [
    path('', accounts.views.profile, name='profile'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    path('signup/', accounts.views.signup, name='signup'),
]