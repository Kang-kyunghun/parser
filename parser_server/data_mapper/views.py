import json
import requests
import boto3
import pandas       as pd

from django.http    import JsonResponse
from django.views   import View

from mapper.data_mapper import data_mapper

class DataMappingView(View):

    def post(self, request):
        #실제 데이터 구조랑 맞춰봐야 됨 (엑셀 받는 주소 때문) 
        
        data_blueprint = json.loads(request.body)
        address_s3 = data_blueprint["googleFormResponseRemoteKey"] 
        
        get_excel = pd.read_excel(address_s3)
        data_mapper(get_excel, data_blueprint)
        result = "OK"
        return JsonResponse({'message':result}, status=200)
        
            # result = "No"
            # return JsonResponse({'message':result}, status=400)
    