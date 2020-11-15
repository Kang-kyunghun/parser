import json
import requests
import boto3
import django_rq
import openpyxl
import pandas           as pd

from django.http        import JsonResponse
from django.views       import View

from mapper.data_mapper import data_mapper
from mapper.exception   import exception_title, exception_empty_data, exception_unexpeted_data
class DataMappingView(View):
    def post(self, request):

        data_blueprint = json.loads(request.body)
        address_s3 = data_blueprint["googleFormResponseRemoteKey"] 
        
        get_excel = pd.read_excel(address_s3)
       
        try:
            #blueprint에서의 제목이 모두 엑셀에 없을 경우
            if exception_title(data_blueprint, get_excel):
                return JsonResponse({'status': '문항 제목이 일치하지 않습니다.'}, status=400)

            # 타임스탬프 외에 데이터가 전혀 없으면 에러
           
            if exception_empty_data(get_excel):
                return JsonResponse({'status': '엑셀 데이터가 없습니다.'}, status=400)
            
            if exception_unexpeted_data(data_blueprint, get_excel):
                return JsonResponse({'status': '답변이 일치하지 않습니다'}, status=200)
            
            q = django_rq.get_queue('default')
            q.empty()
            q.enqueue(data_mapper, get_excel, data_blueprint, result_ttl=30)
            return JsonResponse({'status': 'SUCCESS'}, status=200)
 
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)