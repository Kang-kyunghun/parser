import json

from django.http                    import JsonResponse
from django.views                   import View

class PingView(View):
    def get(self, request):
        
        return JsonResponse({'answer' : 'pong'}, status=200)