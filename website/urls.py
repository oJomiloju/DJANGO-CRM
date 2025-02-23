from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('/about',views.about,name='about'),
    path('/login',views.login_user,name='login'),
    path('/logout',views.logout_user,name='logout'),
    path('/register',views.register_user,name='register'),
    path('record/<int:pk>',views.class_record,name='record'),
    path('delete_record/<int:pk>',views.delete_record,name='delete_record'),
    path('add_record',views.add_record,name='add_record'),
    path('update_record/<int:pk>',views.update_record,name='update_record'),
    path('update_record/<int:pk>',views.update_record,name='update_record'),
    path('record/<int:record_id>/add_homework/', views.add_homework, name='add_homework'), 
    path('record/<int:record_id>/delete_homework/<int:homework_id>/', views.delete_homework, name='delete_homework'),
    path('record/<int:record_id>/update_homework/<int:homework_id>/', views.update_homework, name='update_homework'),
]