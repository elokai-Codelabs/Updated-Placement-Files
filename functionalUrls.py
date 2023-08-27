from .import views
from .excel_to_db import *


from django.urls import path

urlpatterns = [

 path('', views.loginUser, name='login'),
 path('logout/', views.logoutUser, name='logout'),

 path('dashboard/',views.index, name='index' ),
 path('dashboard/program-selection/',views.programs, name='programs-selection' ),
 path('dashboard/placement/',views.placement, name='placement' ),

# READING EXCEL INTO THE DATABASE
path('read_courses/', read_course_excel, name='read_course'),
path('read_programs/', read_program_excel, name='read_program'),

# COURSES
 path('dashboard/courses/',views.show_course, name='courses' ),
 path('dashboard/create-course/',views.create_course, name='create-course' ),
 path('dashboard/edit-course/<str:pk>',views.edit_course, name='edit-course' ),
 path('dashboard/delete-course/<str:pk>',views.delete_course, name='delete-course' ),

#  PROGRAMS
path('dashboard/programs/',views.show_program, name='programs' ),
 path('dashboard/create-program/',views.create_program, name='create-program' ),
 path('dashboard/edit-program/<str:pk>',views.edit_program, name='edit-program' ),
 path('dashboard/delete-program/<str:pk>',views.delete_program, name='delete-program' ),

#  GRADES
path('dashboard/grades/',views.show_grades, name='grades' ),
path('dashboard/create-grade/',views.create_grade, name='create-grade' ),
path('dashboard/edit-grade/<str:pk>',views.edit_grade, name='edit-grade' ),
path('dashboard/delete-grade/<str:pk>',views.delete_grade, name='delete-grade' ),
]