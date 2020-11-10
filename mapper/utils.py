import request_data
import time
import pandas as pd

from uuid import uuid4


def change_time_format(local_time):
    str_time = local_time
    in_time = time.strptime(str_time,'%Y-%m-%d %H:%M:%S.%f')
    unix_time = time.mktime(in_time)
    
    return unix_time

# def matching_type():

def matching_data(body, data_excel):
    
    data_bodies = body
    titles_excel = list(data_excel.columns)
    unmatched_titles = list(titles_excel[1:])
    
    for title_excel in titles_excel[1:]:
        for body in data_bodies:
            if body['title'] == title_excel:
                unmatched_titles.remove(body["title"])
                break
    print(unmatched_titles)
    for unmatched_data in unmatched_titles:
        del data_excel[unmatched_data]
    
    #     if titles_excel[index] == question[index]['title']:
    #         break
    #     else:
    #         unmatched_titles.append(titles_excel[index])
    #         break
    # print(unmatched_titles)
    # answers_all = data_excel
    # answers_all.drop(['기수를 입력해주세요'], axis='columns', inplace=True)
    # print(answers_all)
    # for ansewrs_person in answers_all:
    #     print(ansewrs_person)


    
    # answers_all = data_excel.values
    
    
    
    
    
    # #설문 전체 문항들 제목 list
    # titles = list(data_excel.columns)
    # type_dict = {}

    # for question in data_content['body']:
    #     for index in range(1,len(titles)):
    #         if titles[index] == question['title']:
    #             type_dict[index] = question['type']
    #             break
    

    return data_excel

if __name__ == '__main__':
    
    data_blueprint = request_data.request_data
    data_content = data_blueprint['contents']
    FILE_PATH = './edited_test_data.xlsx'
    data_excel = matching_data(data_content['body'], pd.read_excel(FILE_PATH))
    print(data_excel.columns)