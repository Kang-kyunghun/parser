import json
import requests
import re
import boto3
import wget
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
        blueprint_content = data['contents']
        url = data['googleFormResponseRemoteKey']
        filename = url.split('/')[-1]
        filesave = requests.get(url, allow_redirects=True)
        with open(f'{filename}', 'wb') as local_file:
            local_file.write(filesave.content)
        
        # 엑셀 파일 읽기
        excel_data = pd.read_excel(f'{filename}')
        k = pd.DataFrame(excel_data)
        excel_body_data = k.values
        excel_titles = list(excel_data.columns)

        try:
            blueprint_titles = []
            blueprint_body = []
            excel_answer = list(excel_data.iloc)

            for i in blueprint_content['body']:
                blueprint_titles.append(i['title'])

            for blueprint_title in blueprint_titles:
                if blueprint_title not in excel_titles:
                    return JsonResponse({'status': '문항 제목이 일치하지 않습니다.'}, status=400)

            # 타임스탬프 외에 데이터가 전혀 없으면 에러
            count = 0
            for row in range(len(excel_answer)):
                for col in range(1,len(excel_titles)):
                    if str(excel_body_data[row][col]) != 'nan':
                        break
                    count += 1
            if count == (len(excel_answer) * (len(excel_titles)-1)):
                return JsonResponse({'status': '엑셀 데이터가 없습니다.'}, status=400)
            
            # 문항 제목이 같을 때 blueprint 옵션에 '기타'항목 여부 확인
            for blueprint_body in blueprint_content['body']:
                if blueprint_body['type'] == 'check' or blueprint_body['type'] == 'radio':
                    
                    if '기타:' not in blueprint_body['body']:
                        excel_header_data = []
                        for n in excel_data[blueprint_body['title']]:
                            if str(n) != 'nan':
                                excel_header_data.append(n)
                        print('excel_header_data : ',excel_header_data)
                        for answer in excel_header_data:
                            if answer not in blueprint_body['body']:
                                return JsonResponse({'status': '답변이 일치하지 않습니다'}, status=200)
            return JsonResponse({'status': 'SUCCESS'}, status=200)
 
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)