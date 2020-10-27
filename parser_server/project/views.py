import json
import requests
import re

from django.http                    import JsonResponse
from django.views                   import View


class ParsingView(View):
    def post(self, request):
        

        return JsonResponse({'result':'SUCCESS'}, status=200)