import json
import requests
import re

from django.http                    import JsonResponse
from django.views                   import View

from naver_parser.naver_parser import naver_form
from google_parser.google_parser    import google_form

class ParsingView(View):
    def post(self, request):
        data  = json.loads(request.body)
        url = data['url']
        p_naver = re.compile('naver')
        p_google = re.compile('google')
        p_google_short = re.compile('forms.gle')

        if p_naver.search(url):
            result = naver_form(url)
        elif p_google.search(url) or p_google_short.search(url):
            result = google_form(url)
        else:
            return JsonResponse({'message':'BAD REQUEST'}, status=400)
        
        if not result:
            return JsonResponse({'message':'BAD REQUEST'}, status=400)
        return JsonResponse({'result':result}, status=200)