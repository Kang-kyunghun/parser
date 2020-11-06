import request_data
import pandas as pd
from math import isnan
from uuid import uuid4
from function_mapper import *


data_request = request_data.request_data_radio
data_content = data_request['contents']
FILE_PATH = './test_code_data.xlsx'
data_excel = pd.read_excel(FILE_PATH)

#설문 전체 문항들 제목 list
titles = list(data_excel.columns)
type_dict = {}
response_data = []
uuid = str(uuid4())
for question in data_content['body']:
    for index in range(1,len(titles)):
        if titles[index] == question['title']:
            type_dict[index] = question['type']
            break

# len(data_excel) :  row의 길이
# len(data_excel.columns) :column의 길이
# data_excel.values[row] : 1명이 답한 모든 답
answers_all = data_excel.values
for ansewrs_person in answers_all:
    changed_time = change_time_format(ansewrs_person[0])
    for index in range(1, len(ansewrs_person)):
        data_request = ansewrs_person[index]
        question_type = type_dict[index]
        if question_type == 'radio':
            question_data = mapper_radio(data_request, data_excel, changed_time, uuid)
            response_data.append(question_data)
        elif question_type == 'shorttext':
            question_data = mapper_shorttext(data_request, data_excel, changed_time, uuid)
            response_data.append(question_data)
        elif question_type == 'radio_image_selections':
            question_data = mapper_radio_image_selections(data_request, data_excel, changed_time, uuid)
            response_data.append(question_data)
result = {
    "responseData" : response_data,
    "surveyId"     : data_request["surveyId"],
    "urlToken"     : data_request["urlToken"],
    "uuid"         : uuid,
    "version"      : data_request["version"]
    
}
    

# test_dict ={'type' : mapper_radio(data, data_excel)}
# if data_type == 'radio':
# mapper_radio(data, data_excel)