import request_data
import pandas as pd

def mapper_radio(blueprint_contents, data_excel):
    

    titles = list(data_excel.columns)
    for row in range(len(data_excel)):
        val = str(data_excel.values[row][2])
        print(val)



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
    data = request_data.request_data_radio
    data_contents = data['contents']
    FILE_PATH = 'test_data.xlsx'
    data_excel = pd.read_excel(FILE_PATH)
    mapper_radio(data_contents, data_excel)