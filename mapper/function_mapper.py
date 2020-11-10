import request_data
import time
import pandas as pd
from math import isnan
from uuid import uuid4
from utils import change_time_format


def mapper_radio(data_blueprint, data_excel, data_answer,  unix_time, uuid):
    answer = data_answer["answer"]
    if str(type(answer)) == "<class 'float'>" :
        answer = ""
    order = data_answer["order"] -1
    body = data_blueprint["contents"]["body"][order]
    selections = body["body"]
    has_etc = False
    is_etc = False
    etc_input = None
    
    if "기타:" in selections:
        has_etc = True
   
    if answer:
        if not data_answer["answer"] in selections:
            is_etc = True
            etc_input = data_answer["answer"]
    
    mapping = {
        "answered_text": str(answer),
        "created_at": unix_time,
        "duration": 1.0,
        "etc_input": etc_input,
        "finished_at": unix_time + 1.0,
        "has_etc": has_etc,
        "is_etc": is_etc,
        "metadata": {},
        "phone": "01000000000",
        "question_order": order,
        "question_text": body["title"],
        "question_type": "radio",
        "selections": selections,
        "started_at": unix_time,
        "survey_id": data_blueprint["surveyId"],
        "user_key": "",
        "uuid": uuid,
        "version": data_blueprint["version"]
    }
    return mapping

def mapper_radio_image_selections(data_blueprint, data_excel, data_answer,  unix_time, uuid):
    answer = data_answer["answer"]
    if str(type(answer)) == "<class 'float'>" :
        answer = ""
    order = data_answer["order"] -1
    body = data_blueprint["contents"]["body"][order]
    selections = body["body"]
    image_selections = body["image_selections"]
    has_etc = False
    is_etc = False
    etc_input = None
    
    if "기타:" in selections:
        has_etc = True
        
    if answer :
        if not data_answer["answer"] in selections:
            is_etc = True
            etc_input = data_answer["answer"]
    
    mapping = {
        "answered_text": str(answer),
        "created_at": unix_time,
        "duration": 1.0,
        "etc_input": etc_input,
        "finished_at": unix_time + 1.0,
        "has_etc": has_etc,
        "image_selections" : image_selections,
        "is_etc": is_etc,
        "metadata": {},
        "phone": "01000000000",
        "question_order": order,
        "question_text": body["title"],
        "question_type": "radio_image_selections",
        "selections": selections,
        "started_at": unix_time,
        "survey_id": data_blueprint["surveyId"],
        "user_key": "",
        "uuid": uuid,
        "version": data_blueprint["version"]
    }
    return mapping

def mapper_check(data_blueprint, data_excel, data_answer,  unix_time, uuid):
    order = data_answer["order"] -1
    body = data_blueprint["contents"]["body"][order]
    selections = body["body"]
    sel_ranges = {"max" : len(selections), "min" : 1}
    has_etc = False
    is_etc = False
    etc_input = None

    if "기타:" in selections:
        has_etc = True

    if str(type(data_answer["answer"])) == "<class 'float'>" :
        answered_text = ''    
    else:
        answers = data_answer["answer"].split(', ')
        sel_order = []
        
        for answer in answers:
            if not answer in selections:
                etc_input = answer
                is_etc = True
                answers.remove(etc_input)
                sel_order.append(str(selections.index("기타:")))
            else:
                sel_order.append(str(selections.index(answer)+1))
        
        answered_text = ','.join(sel_order) if not etc_input else ','.join(sel_order) + '|' + etc_input

    mapping = {
        "answered_text": str(answered_text),
        "created_at": unix_time,
        "duration": 1.0,
        "etc_input": etc_input,
        "finished_at": unix_time + 1.0,
        "has_etc": has_etc,
        "is_etc": is_etc,
        "metadata": {},
        "phone": "01000000000",
        "question_order": order,
        "question_text": body["title"],
        "question_type": "check",
        "sel_ranges" : sel_ranges,
        "selections": selections,
        "started_at": unix_time,
        "survey_id": data_blueprint["surveyId"],
        "user_key": "",
        "uuid": uuid,
        "version": data_blueprint["version"]
    }
    return mapping

def mapper_check_image_selections(data_blueprint, data_excel, data_answer,  unix_time, uuid):
    order = data_answer["order"] -1
    body = data_blueprint["contents"]["body"][order]
    selections = body["body"]
    image_selections = body["image_selections"]
    sel_ranges = {"max" : len(selections), "min" : 1}
    has_etc = False
    is_etc = False
    etc_input = None
    
    if "기타:" in selections:
        has_etc = True
    
    if str(type(data_answer["answer"])) == "<class 'float'>" :
        answered_text = ''
    else:
        answers = data_answer["answer"].split(', ')
        sel_order = []
        
        for answer in answers:
            if not answer in selections:
                etc_input = answer
                is_etc = True
                answers.remove(etc_input)
                sel_order.append(str(selections.index("기타:")))
            else:
                sel_order.append(str(selections.index(answer)+1))
        
        answered_text = ','.join(sel_order) if not etc_input else ','.join(sel_order) + '|' + etc_input
    
    mapping = {
        "answered_text": str(answered_text),
        "created_at": unix_time,
        "duration": 1.0,
        "etc_input": etc_input,
        "finished_at": unix_time + 1.0,
        "has_etc": has_etc,
        "image_selections" : image_selections,
        "is_etc": is_etc,
        "metadata": {},
        "phone": "01000000000",
        "question_order": order,
        "question_text": body["title"],
        "question_type": "check_image_selections",
        "sel_ranges" : sel_ranges,
        "selections": selections,
        "started_at": unix_time,
        "survey_id": data_blueprint["surveyId"],
        "user_key": "",
        "uuid": uuid,
        "version": data_blueprint["version"]
    }
    return mapping

def mapper_shorttext(data_blueprint, data_excel, data_answer,  unix_time, uuid):
    answer = data_answer["answer"]
    if str(type(answer)) == "<class 'float'>" :
        answer = ""
    order = data_answer["order"] -1
    body = data_blueprint["contents"]["body"][order]
    
    mapping = {
        "answered_text": str(answer),
        "created_at": unix_time,
        "duration": 1.0,
        "etc_input": None,
        "finished_at": unix_time + 1.0,
        "has_etc": False,
        "is_etc": False,
        "metadata": {},
        "phone": "01000000000",
        "question_order": order,
        "question_text": body["title"],
        "question_type": "shorttext",
        "selections": "",
        "started_at": unix_time,
        "survey_id": data_blueprint["surveyId"],
        "user_key": "",
        "uuid": uuid,
        "version": data_blueprint["version"]
    }
    return mapping

if __name__ == '__main__':
    
    
    data_blueprint = request_data.request_data_check
    data_content = data_blueprint['contents']
    FILE_PATH = './test_code_data.xlsx'
    data_excel = pd.read_excel(FILE_PATH)
    unix_time = change_time_format('2020-11-04 11:03:29.053000')
    data_answer ={
        "order" : 1,
        "answer": "프론트엔드, 자바스크립트, 리액트, RN"

    }
    uuid = "uuid"
    
    mapping = mapper_check(data_blueprint, data_excel, data_answer,  unix_time, uuid)#mapper_check(data_blueprint, data_excel, data_answer,  unix_time, uuid)
    print(mapping)
    