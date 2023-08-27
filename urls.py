
from django.urls import path
from . import views
from .excel_to_db import *

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('dashboard/', views.IndexView.as_view(), name='index'),
    path('dashboard/program-selection/', views.ProgramsView.as_view(), name='programs-selection'),
    path('dashboard/placement/', views.PlacementView.as_view(), name='placement'),

# READING EXCEL INTO THE DATABASE
path('read_courses/', read_course_excel, name='read_course'),
path('read_programs/', read_program_excel, name='read_program'),

    # COURSES
    path('dashboard/courses/', views.ShowCourseView.as_view(), name='courses'),
    path('dashboard/create-course/', views.CreateCourseView.as_view(), name='create-course'),
    path('dashboard/edit-course/<str:pk>/', views.EditCourseView.as_view(), name='edit-course'),
    path('dashboard/delete-course/<str:pk>/', views.DeleteCourseView.as_view(), name='delete-course'),

    # PROGRAMS
    path('dashboard/programs/', views.ShowProgramView.as_view(), name='programs'),
    path('dashboard/create-program/', views.CreateProgramView.as_view(), name='create-program'),
    path('dashboard/edit-program/<str:pk>/', views.EditProgramView.as_view(), name='edit-program'),
    path('dashboard/delete-program/<str:pk>/', views.DeleteProgramView.as_view(), name='delete-program'),

    # GRADES
    path('dashboard/grades/', views.ShowGradesView.as_view(), name='grades'),
    path('dashboard/create-grade/', views.CreateGradeView.as_view(), name='create-grade'),
    path('dashboard/edit-grade/<str:pk>/', views.EditGradeView.as_view(), name='edit-grade'),
    path('dashboard/delete-grade/<str:pk>/', views.DeleteGradeView.as_view(), name='delete-grade'),
         
]
