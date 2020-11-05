from django.urls import path

from parserdata.views import ParserdataView

urlpatterns = [
    path('/upload', ParserdataView.as_view()),
]