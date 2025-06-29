from django.urls import path
from .views import (
    personaTestView,
    personaCreateView,
    personaDeleteView,
    personaListView,
    searchForHelp,
    personasShowObject,
    personaDetailView,
)

app_name = 'personas'
urlpatterns = [
    path('add/', personaCreateView, name = 'adding'),
    path('', personaListView.as_view(), name = 'Listing'),
    path('<int:pk>/', personaDetailView.as_view(), name='persona-detail'),
    path('<int:myID>/delete/', personaDeleteView, name='deleting'),
]
