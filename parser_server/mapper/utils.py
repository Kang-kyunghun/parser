from mapper.request_data import request_data
import json
import boto3
import time
import pandas as pd

from uuid import uuid4

#s3 업로드
def s3_uploader(result):
    s3_client = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    file = json.dumps(result, indent="\t", ensure_ascii=False)
   
    s3_client.put_object(
        Body=str(file),
        Bucket="upload-data-jack",
        Key=f"{result['surveyId']}/{result['responseData'][0]['uuid']}.json"
    )
#local time change to unix time
def change_time_format(local_time):
    str_time = local_time
    in_time = time.strptime(str_time,'%Y-%m-%d %H:%M:%S.%f')
    unix_time = time.mktime(in_time)
    
    return unix_time
#blueprint와 엑셀의 제목을 비교하여 해당 제목의 타입 결정
def matching_type(body_blueprint, data_excel):
    data_bodies = body_blueprint
    titles_excel = list(data_excel.columns)
 
    type_dict = {}
    
    for title_excel in titles_excel[1:]:
        for body in data_bodies:
            if body['title'] == title_excel:
                type_dict[titles_excel.index(title_excel)] = body['type']
                break

    return type_dict

# bluprint의 문항 순서에 맞게 엑셀 데이터 재배치
def matching_data(body_blueprint, get_excel):
    
    data_bodies = body_blueprint
    titles_excel = list(get_excel.columns)
    unmatched_titles = list(titles_excel[1:])
    titles_blueprint = []
    for body in data_bodies:
        titles_blueprint.append(body['title'])
    
    for title_excel in titles_excel[1:]:
        for title_blueprint in titles_blueprint:
            if title_blueprint == title_excel:
                unmatched_titles.remove(title_excel)
                break
    
    for unmatched_data in unmatched_titles:
        del get_excel[unmatched_data]
    data_excel = get_excel[['타임스탬프']+titles_blueprint]
    return data_excel
