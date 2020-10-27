import json
import requests
import re

from django.http                    import JsonResponse
from django.views                   import View

from naver_parser.naver_parser import naver_form
from google_parser.goolge_parser    import google_form





class ParsingView(View):
    def post(self, request):
        data  = json.loads(request.body)
        url = data['url']
        #result = naver_form(url)
        result = google_form(url)

        return JsonResponse({'result':result}, status=200)