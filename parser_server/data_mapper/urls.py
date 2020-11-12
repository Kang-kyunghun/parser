from django.urls import path

from .views      import DataMappingView

urlpatterns = [
    path('/mapper', DataMappingView.as_view()),
     
]