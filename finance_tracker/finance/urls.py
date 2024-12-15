from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('goals/', views.goals, name='goals'),
    path('add-goal/', views.add_goal, name='add_goal'),
    path('reports/', views.reports, name='reports'),
]
