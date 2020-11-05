import json
import requests
import re
import boto3
import openpyxl
import pandas as pd
from django.http                    import JsonResponse
from django.views                   import View

class ParserdataView(View):
    def post(self, request):
        data  = json.loads(request.body)
        # surveyid = data['surveyId']
        # urltoken = data['urlToken']
        # version = data['version']
        blueprint_content = data['content']
        url = data['googleFormResponseRemoteKey']
        filename = url.split('/')[-1]
        r = requests.get(url, allow_redirects=True)
        test = pd.read_excel('./testexcel.xlsx')
        # open(filename, 'wb').write(r.content)
        # wb = openpyxl.load_workbook('./testexcel.xlsx', data_only=True)
        
        print(test)
        body_list = []
        # {'contents': {'survey_title': '모든 타입 설문', 'body': [{'type': 'radio', 'title': '객관식 단일2'}, {'type': 'radio', 'title': '객관식 단일3'}, {'type': 'radio', 'title': '객관식 단일4'}, {'type': 'radio', 'title': '객관식 단일5'}]}}
        for i in blueprint_content.get('contents')['body']:
            body_list.append(i['title'])
        
        # # print(file)
        print("블루프린트 : ", body_list) # 블루프린트 제목 모음




        return JsonResponse({'message':'success'}, status=200)

