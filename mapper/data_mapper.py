import request_data
import pandas as pd
from math import isnan
from uuid import uuid4
from function_mapper import *


data_blueprint = request_data.request_data
data_content = data_blueprint['contents']
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
print(type_dict)
# len(data_excel) :  row의 길이
# len(data_excel.columns) :column의 길이
# data_excel.values[row] : 1명이 답한 모든 답
answers_all = data_excel.values
for ansewrs_person in answers_all:
    changed_time = change_time_format(ansewrs_person[0])
    for index in range(1, len(ansewrs_person)):
        data_answer = {
                "answer" : ansewrs_person[index],
                "order"  : index
            }
        question_type = type_dict[index]
        
        if question_type == 'radio':
            question_data = mapper_radio(data_blueprint, data_excel, data_answer, changed_time, uuid)
            response_data.append(question_data)
        
        elif question_type == 'shorttext':
            question_data = mapper_shorttext(data_blueprint, data_excel, data_answer,  changed_time, uuid)
            response_data.append(question_data)
        
        elif question_type == 'radio_image_selections':
            question_data = mapper_radio_image_selections(data_blueprint, data_excel, data_answer,  changed_time, uuid)
            response_data.append(question_data)
result = {
    "responseData" : response_data,
    "surveyId"     : data_blueprint["surveyId"],
    "urlToken"     : data_blueprint["urlToken"],
    "uuid"         : uuid,
    "version"      : data_blueprint["version"]
    
}
    

print(result)