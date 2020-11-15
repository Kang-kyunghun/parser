from request_data import request_data
import pandas           as pd

from utils import matching_data
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
  
if __name__ == '__main__':

    body_blueprint = request_data
    get_excel = pd.read_excel("https://upload-data-jack.s3.ap-northeast-2.amazonaws.com/edited_test_data.xlsx")
    # get_excel = pd.read_excel("https://upload-data-jack.s3.ap-northeast-2.amazonaws.com/empty_data.xlsx")
   

    
    # result = exception_title(body_blueprint, get_excel)
    # result = matching_data(body_blueprint, get_excel)
    # print(result) 
    data = get_excel
    print(exception_empty_data(data))