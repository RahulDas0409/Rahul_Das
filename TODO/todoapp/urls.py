from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('addtodos', views.addtodos, name='Add Todos'),
    path('updatetodos/<str:pk>/',views.updatetodos, name="Update Todo"),
    path('deletetodos/<str:pk>/',views.deletetodos, name="Delete Todo"),
    path('signin', views.signin, name='Sign In'),
    path('log_in', views.log_in, name='Log In'),
    path('log_out', views.log_out, name='Log Out'),
]
