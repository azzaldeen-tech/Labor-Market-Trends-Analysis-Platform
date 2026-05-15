from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _
app_name = 'core'

# تأكد أن الاسم urlpatterns بالجمع (s في النهاية) وكل الحروف small
urlpatterns = [
    path('', views.home, name='home'),
    path('labor_market_trends/', views.labor_market_trends, name='labor_market_trends'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
    path('search/', views.search_users, name='search_users'),
    # path('live_jobs_view/', views.live_jobs_view, name='live_jobs_view'),
    path('search_skills', views.search_skills, name='search_skills'),
    path('search_jobs', views.search_jobs, name='search_jobs'),
]