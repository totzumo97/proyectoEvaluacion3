from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('perfiles/',  views.API_objects.as_view()),
    path('perfiles/<int:pk>/', views.API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)