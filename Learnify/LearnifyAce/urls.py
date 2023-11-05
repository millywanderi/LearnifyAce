from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login, name='login'),
    path('staff/', views.staff, name="staff"),
    path('delete-course/<int:pk>', views.delete_course, name="delete-course"),
    path('all-lessons/', views.all_lessons, name="all-lessons"),
    path('delete-lesson/<int:pk>', views.delete_lesson, name="delete-lesson"),
    path('edit-course/<int:pk>', views.edit_course, name="edit-course"),
    path('edit-lesson/<int:pk>', views.edit_lesson, name="edit-lesson"),
    path('course-register/<int:pk>', views.register_course, name='course-register'),
    path('logout/', views.logout, name='logout'),
    path('classroom/<int:pk>', views.classroom, name="classroom"),
    
]
