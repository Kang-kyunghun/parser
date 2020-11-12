from django.urls import path

from .views      import DataMappingView

urlpatterns = [
    path('', DataMappingView.as_view()),
     
]