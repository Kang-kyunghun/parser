from django.urls import path

from project.views import ParsingView

urlpatterns = [
    path('/form', ParsingView.as_view()),
]
