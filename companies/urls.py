from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('search_skills', views.search_skills, name='search_skills'),
    path('job/add/', views.manage_job, name='job_add'),
    path('job/edit/<int:pk>/', views.manage_job, name='job_edit'),
    path('advertised_jobs', views.advertised_jobs, name='advertised_jobs'),
    path('jobs_applications', views.jobs_applications, name='job_apps'),
]
