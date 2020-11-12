# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('parser', include('project.urls')),
    path('mapper', include('data_mapper.urls')),
    path("django-rq/", include("django_rq.urls")),
    path('data', include('parserdata.urls')),
    path('', include('ping.urls'))
]
