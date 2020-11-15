from request_data import request_data
import pandas           as pd
import re
from utils import matching_data, matching_type
def exception_title(data_blueprint, get_excel):
    
    bodies_blueprint = data_blueprint['contents']['body']
    titles_excel = list(get_excel.columns)
  
    titles_blueprint = []
    for body in bodies_blueprint:
        titles_blueprint.append(body['title'])

    
    for title_blueprint in titles_blueprint:
        if not title_blueprint in titles_excel:
            return True
    return False

def exception_empty_data(get_excel):
    answers =  get_excel.values
    for index in range(len(answers)):
        for answer in answers[index][1:]:
            if not str(answer) == 'nan':
                return False
    return True

def exception_unexpeted_data(data_blueprint, get_excel):
    
    data_blueprint_body = data_blueprint['contents']['body']
    data_excel = matching_data(data_blueprint_body, get_excel)
   
    p_radio = re.compile('radio')
    p_check = re.compile('check')
    
    titles_blueprint = []
    for body in data_blueprint_body:
        titles_blueprint.append(body['title'])

    for body in data_blueprint_body:
        question_type = body['type']
        question_title = body['title']
        question_selections = body['body']
        if not (p_radio.search(question_type) or p_check.search(question_type)):
           continue
        
        if "기타:" in question_selections:
            continue
        
        if p_radio.search(question_type):
            for index in range(len(data_excel.values)):
                answer = data_excel.values[index][titles_blueprint.index(question_title)+1]
                if (not str(answer) in question_selections) and (str(answer) != 'nan'):
                    return True
        
        if p_check.search(question_type):
            print(question_selections)
            for index in range(len(data_excel.values)):
                answers = data_excel.values[index][titles_blueprint.index(question_title)+1].split(',')
                for answer in answers:
                    if answer[0] == ' ':
                        answer = answer[1:]
                    if (not str(answer) in question_selections) and (str(answer) != 'nan'):
                        return True

    return False
  
if __name__ == '__main__':

    data_blueprint = request_data
    get_excel = pd.read_excel("https://upload-data-jack.s3.ap-northeast-2.amazonaws.com/edited_test_data.xlsx")
    # get_excel = pd.read_excel("https://upload-data-jack.s3.ap-northeast-2.amazonaws.com/empty_data.xlsx")
   

    
    # result = exception_title(body_blueprint, get_excel)
    result = exception_unexpeted_data(data_blueprint, get_excel)
    print(result) 
    # data = get_excel.values[1][1] #앞: 사람, 뒤: 문항
    # print(data)