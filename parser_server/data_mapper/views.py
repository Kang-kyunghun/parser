import json
import requests
import boto3
import django_rq
import openpyxl
import pandas           as pd

from django.http        import JsonResponse
from django.views       import View

from mapper.data_mapper import data_mapper
from mapper.exception   import exception_title, exception_empty_data
class DataMappingView(View):
    def post(self, request):

        data_blueprint = json.loads(request.body)
        address_s3 = data_blueprint["googleFormResponseRemoteKey"] 
        
        get_excel = pd.read_excel(address_s3)
       
        blueprint_content = data_blueprint['contents']
    
        data_excel = pd.DataFrame(get_excel)
        excel_body_data = data_excel.values
        excel_titles = list(get_excel.columns)
        excel_answer = list(get_excel.iloc)
        try:
            #blueprint에서의 제목이 모두 엑셀에 없을 경우
            if exception_title(data_blueprint, get_excel):
                return JsonResponse({'status': '문항 제목이 일치하지 않습니다.'}, status=400)

            # 타임스탬프 외에 데이터가 전혀 없으면 에러
           
            if exception_empty_data(get_excel):
                return JsonResponse({'status': '엑셀 데이터가 없습니다.'}, status=400)
            
            # 문항 제목이 같을 때 blueprint 옵션에 '기타'항목 여부 확인
            for blueprint_body in blueprint_content['body']:
                if blueprint_body['type'] == 'check' or blueprint_body['type'] == 'radio':
                    
                    if '기타:' not in blueprint_body['body']:
                        excel_header_data = []
                        for n in get_excel[blueprint_body['title']]:
                            if str(n) != 'nan':
                                excel_header_data.append(n)
                        print('excel_header_data : ',excel_header_data)
                        for answer in excel_header_data:
                            if answer not in blueprint_body['body']:
                                return JsonResponse({'status': '답변이 일치하지 않습니다'}, status=200)
            
            q = django_rq.get_queue('default')
            q.empty()
            q.enqueue(data_mapper, get_excel, data_blueprint, result_ttl=30)
            return JsonResponse({'status': 'SUCCESS'}, status=200)
 
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)