from django.urls import path
from .views import (
    personaTestView,
    personaCreateView,
    personaDeleteView,
    personaListView,
    searchForHelp,
    personasShowObject,
    personaDetailView,
    personaCreateView,
    personaUpdateView,
)

app_name = 'personas'
urlpatterns = [
    path('<int:pk>/update/', personaUpdateView.as_view(), name="persona-update"),
    path('create/', personaCreateView.as_view(), name = 'persona-create'),
    path('', personaListView.as_view(), name = 'Listing'),
    path('<int:pk>/', personaDetailView.as_view(), name='persona-detail'),
    path('<int:pk>/delete/', personaDeleteView.as_view(), name='persona-delete'),
]
