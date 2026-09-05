from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('skills/', views.skill_list, name='skill_list'),
    path('contact/', views.contact, name='contact'),

    # Dashboard (login required) — add/edit/delete Projects & Skills from the site itself.
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile/', views.profile_update, name='profile_update'),

    path('dashboard/projects/add/', views.project_create, name='project_create'),
    path('dashboard/projects/<int:pk>/edit/', views.project_update, name='project_update'),
    path('dashboard/projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

    path('dashboard/skills/add/', views.skill_create, name='skill_create'),
    path('dashboard/skills/<int:pk>/edit/', views.skill_update, name='skill_update'),
    path('dashboard/skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
]
