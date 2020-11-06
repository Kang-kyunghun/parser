import request_data
import time
import pandas as pd
from math import isnan
from uuid import uuid4

# len(data_excel) :  row의 길이
# len(data_excel.columns) :column의 길이
# data_excel.values[row] : 1명이 답한 모든 답
def mapper_radio(data_blueprint, data_excel, data_answer,  changed_time, uuid):
    order = data_answer["order"]
    body = data_blueprint["contents"]["body"][order - 1]
    selections = body["body"]
    has_etc = False
    is_etc = False
    if "기타:" in selections:
        has_etc = True
    if not data_answer["answer"] in selections:
        is_etc = True
    mapping = {
        "answered_text": data_answer["answer"],
        "created_at": changed_time,
        "duration": 1.0,
        "etc_input": None,
        "finished_at": changed_time + 1.0,
        "has_etc": has_etc,
        "is_etc": is_etc,
        "metadata": {},
        "phone": "01000000000",
        "question_order": order,
        "question_text": body["title"],
        "question_type": "radio",
        "selections": selections,
        "started_at": changed_time,
        "survey_id": data_blueprint["surveyId"],
        "user_key": "",
        "uuid": uuid,
        "version": data_blueprint["version"]
    }
    return mapping

def mapper_shorttext(data_blueprint, data_excel, data_answer,  changed_time, uuid):
    order = data_answer["order"]
    body = data_blueprint["contents"]["body"][order - 1]
    mapping = {
        "answered_text": data_answer["answer"],
        "created_at": changed_time,
        "duration": 1.0,
        "etc_input": None,
        "finished_at": changed_time + 1.0,
        "has_etc": False,
        "is_etc": False,
        "metadata": {},
        "phone": "01000000000",
        "question_order": order,
        "question_text": body["title"],
        "question_type": "shorttext",
        "selections": "",
        "started_at": changed_time,
        "survey_id": data_blueprint["surveyId"],
        "user_key": "",
        "uuid": uuid,
        "version": data_blueprint["version"]
    }
    return mapping

def mapper_radio_image_selections(data_blueprint, data_answer,  data_excel, changed_time, uuid):
    print('mapper_radio_image_selections')
    return {}

def change_time_format(local_time):
 
    # str_time = '2016-04-25 13:03:17'
    str_time = local_time
    in_time = time.strptime(str_time,'%Y-%m-%d %H:%M:%S')
    changed_time = time.mktime(in_time)
    
    return changed_time




    # mapping = {
    #     "answered_text": "선택하면 5번으로 갑니다",
    #     "created_at": "timestemp",
    #     "duration": 1,
    #     "etc_input": null,
    #     "finished_at": timestemp + 1,
    #     "has_etc": "문항에 기타가 있는지 확인",
    #     "is_etc": "기타문항으로 답했는지 확인",
    #     "metadata": {},
    #     "phone": "01000000000",
    #     "question_order": 0 ,
    #     "question_text": "객관식 단일",
    #     "question_type": "radio",
    #     "selections": ["1", "2", "선택하면 5번으로 갑니다", "4",   "기타:"],
    #     "started_at": "timestemp",
    #     "survey_id": "613547",
    #     "user_key": "",
    #     "uuid": "8c2f3563-b70d-476a-9c63-a5cb54efb672",
    #     "version": 2
    # }


if __name__ == '__main__':
    
    
    data_blueprint = request_data.request_data_radio
    data_content = data_blueprint['contents']
    FILE_PATH = './test_code_data.xlsx'
    data_excel = pd.read_excel(FILE_PATH)
    changed_time = change_time_format('2020-10-25 13:03:18')
    data_answer ={
        "order" : 1,
        "answer": "브랜디"

    }
    uuid = "uuid"
    
    mapping = mapper_radio(data_blueprint, data_excel, data_answer,  changed_time, uuid)
    print(mapping)
    