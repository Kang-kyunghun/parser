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
  
if __name__ == '__main__':

    body_blueprint = request_data
    get_excel = pd.read_excel("https://upload-data-jack.s3.ap-northeast-2.amazonaws.com/test_code_data2.xlsx")

    
    result = exception_title(body_blueprint, get_excel)
    # result = matching_data(body_blueprint, get_excel)
    print(result)  