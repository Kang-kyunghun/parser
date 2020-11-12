import json
import boto3
import time
import pandas as pd
import request_data
from uuid import uuid4

def s3_uploader(result):
    s3_client = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    file = json.dumps(result, indent="\t", ensure_ascii=False)
    googleFormResponse = 'url' #엑셀이 저장된 버킷 주소 받아야됨
    #googleFormResponse = 
    s3_client.put_object(
        Body=str(file),
        Bucket="upload-data-jack",
        Key=f"{result['surveyId']}/{googleFormResponse}__{result['surveyId']}__{result['version']}__{result['responseData'][0]['uuid']}.json"
    )

def change_time_format(local_time):
    str_time = local_time
    in_time = time.strptime(str_time,'%Y-%m-%d %H:%M:%S.%f')
    unix_time = time.mktime(in_time)
    
    return unix_time

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

def matching_data(body_blueprint, data_excel):
    
    data_bodies = body_blueprint
    titles_excel = list(data_excel.columns)
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
        del data_excel[unmatched_data]
    data_excel = data_excel[['타임스탬프']+titles_blueprint]
    return data_excel

if __name__ == '__main__':
    
    data_blueprint = request_data.request_data
    data_content = data_blueprint['contents']
    FILE_PATH = './edited_test_data.xlsx'
    data_excel = matching_data(data_content['body'], pd.read_excel(FILE_PATH))
    print(list(data_excel.columns))