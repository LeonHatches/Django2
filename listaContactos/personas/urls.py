from django.urls import path
from .views import (
    personaTestView,
    personaCreateView,
    personaDeleteView,
    personaListView,
    searchForHelp,
    personasShowObject
)

app_name = 'personas'
urlpatterns = [
    path('add/', personaCreateView, name = 'adding'),
    path('', personaListView.as_view(), name = 'Listing'),
    path('<int:myID>/', personasShowObject, name='browsing'),
    path('<int:myID>/delete/', personaDeleteView, name='deleting'),
]
