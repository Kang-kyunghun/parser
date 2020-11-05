# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('parser', include('project.urls')),
    path('data', include('parserdata.urls')),
    path('', include('ping.urls'))
]
