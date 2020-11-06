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
    # answers = []
    # for row in range(len(data_excel)):
    #     val = data_excel.values[row]
    #     # print(val)
    #     answers.append(val)
    # print(answers[0][0])
    # blank = answers[-1][-1]
    # if isnan(blank):
    #     print('value is none')
    # print(type(blank))

def mapper_shorttext(data_request, data_excel, changed_time, uuid):
    print('mapper_shorttext')
    return {}

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