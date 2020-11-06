import request_data
import pandas as pd
from math import isnan
from uuid import uuid4

# len(data_excel) :  row의 길이
# len(data_excel.columns) :column의 길이
# data_excel.values[row] : 1명이 답한 모든 답
def mapper_radio(data_request, data_excel, changed_time, uuid):
    print('mapper_radio')
    return {}

def mapper_shorttext(data_request, data_excel, changed_time, uuid):
    mapping = {
        "answered_text": data_request["answer"],
        "created_at": changed_time,
        "duration": 1.0,
        "etc_input": None,
        "finished_at": data_request + 1.0,
        "has_etc": False,
        "is_etc": False,
        "metadata": {},
        "phone": "01000000000",
        "question_order": data_request["order"],
        "question_text": data_request["body"]["title"],
        "question_type": "shorttext",
        "selections": "",
        "started_at": changed_time,
        "survey_id": data_request["surveyId"],
        "user_key": "",
        "uuid": uuid,
        "version": data_request["version"]
    }
    return mapping

def mapper_radio_image_selections(data_request, data_excel, changed_time, uuid):
    print('mapper_radio_image_selections')
    return {}

def change_time_format(local_time):
    return 1111




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
    pass