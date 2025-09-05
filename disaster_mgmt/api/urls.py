from django.urls import path
from . import views

urlpatterns = [
    # Frontend Pages
    path('', views.home, name='home'),
    path('resources/page/', views.resources_page, name='resources_page'),
    path('requests/page/', views.requests_page, name='requests_page'),
    path('assessments/page/', views.assessments_page, name='assessments_page'),
    path('assignments/page/', views.assignments_page, name='assignments_page'),

    # API Endpoints
    path('resources/', views.list_resources, name='list_resources'),
    path('resources/add/', views.add_resource, name='add_resource'),
    path('requests/', views.list_requests, name='list_requests'),
    path('assessments/', views.list_assessments, name='list_assessments'),
    path('assignments/', views.list_assignments, name='list_assignments'),
]
