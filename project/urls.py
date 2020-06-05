from django.urls import path
from . import views


urlpatterns = [
    path('<int:project_id>/', views.project_detail, name='detail'),
]