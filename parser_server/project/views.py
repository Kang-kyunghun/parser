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
        p_naver = re.compile('naver.me')
        p_google = re.compile('docs.google.com/form')
        p_google_short = re.compile('forms.gle')

        if p_naver.search(url):
            contents = naver_form(url)
            form_type = 'naver'
        elif p_google.search(url) or p_google_short.search(url):
            contents = google_form(url)
            form_type = 'google'
        else:
            return JsonResponse({'message':'지원하지 않는 URL입니다.'}, status=400)
        
        if not contents['body']:
            return JsonResponse({'message':'공유 권한을 확인해주세요.'}, status=401)
        return JsonResponse({'type'     : form_type,
                             'contents' : contents}, status=200)
