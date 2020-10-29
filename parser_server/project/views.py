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
        p_naver = re.compile('naver')
        p_google = re.compile('google')
        p_google_short = re.compile('forms.gle')

        if p_naver.search(url):
            contents = naver_form(url)
        elif p_google.search(url) or p_google_short.search(url):
            contents = google_form(url)
        else:
            return JsonResponse({'message':'BAD REQUEST'}, status=400)
        
        if not contents['body']:
            return JsonResponse({'message':'BAD REQUEST'}, status=400)
        return JsonResponse({'contents' : contents}, status=200)