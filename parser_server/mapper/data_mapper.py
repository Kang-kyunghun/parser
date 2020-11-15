import pandas as pd
import json
from math import isnan
from uuid import uuid4
from django_rq import job
from function_mapper import (mapper_radio,
                             mapper_check,
                             mapper_radio_image_selections,
                             mapper_check_image_selections,
                             mapper_shorttext)

from utils import change_time_format, matching_data, matching_type, s3_uploader

def data_mapper(get_excel, data_blueprint):
   
    data_blueprint_body = data_blueprint['contents']['body']
    
    data_excel = matching_data(data_blueprint_body, get_excel)
    
    type_dict = matching_type(data_blueprint_body, data_excel)
    
    answers_all = data_excel.values

    # len(data_excel) :  row의 길이
    # len(data_excel.columns) :column의 길이
    # data_excel.values[row] : 1명이 답한 모든 답
    for ansewrs_person in answers_all:
        unix_time = change_time_format(str(ansewrs_person[0]))
        result = {}
        response_data = []
        uuid = str(uuid4())
        
        for index in range(1, len(ansewrs_person)):
            data_answer = {
                    "answer" : ansewrs_person[index],
                    "order"  : index
                }
            question_type = type_dict[index]
            
            if question_type == 'radio':
                question_data = mapper_radio(data_blueprint, data_excel, data_answer, unix_time, uuid)
                response_data.append(question_data)
            
            elif question_type == 'shorttext':
                question_data = mapper_shorttext(data_blueprint, data_excel, data_answer,  unix_time, uuid)
                response_data.append(question_data)
            
            elif question_type == 'radio_image_selections':
                question_data = mapper_radio_image_selections(data_blueprint, data_excel, data_answer,  unix_time, uuid)
                response_data.append(question_data)

            elif question_type == 'check':
                question_data = mapper_check(data_blueprint, data_excel, data_answer,  unix_time, uuid)
                response_data.append(question_data)
            
            elif question_type == 'check_image_selections':
                question_data = mapper_check_image_selections(data_blueprint, data_excel, data_answer,  unix_time, uuid)
                response_data.append(question_data)
        
        result = {
            "responseData" : response_data,
            "surveyId"     : data_blueprint["surveyId"],
            "urlToken"     : data_blueprint["urlToken"],
            "uuid"         : uuid,
            "version"      : data_blueprint["version"]   
        }
    
        s3_uploader(result)
