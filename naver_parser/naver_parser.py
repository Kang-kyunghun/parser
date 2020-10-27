# naver_parser

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def parsing_naver(URL):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(URL)
    time.sleep(2)

    type_pocket = {
        "formItemPh singleChoice vertical"   : "radio",
        "formItemPh multipleChoice vertical" : "check",
        "formItemPh text"                    : "shorttext",
        "formItemPh paragraph"               : "shorttext",
        "formItemPh selectBox"               : "radio",
        "formItemPh scale"                   : "radio",
        "formItemPh grid"                    : "grid radio",
        "formItemPh image"                   : "shorttext",
        "formItemPh file"                    : "shorttext",
        "formItemPh datetime"                : "shorttext",
        "formItemPh phone"                   : "shorttext",
        "formItemPh address"                 : "shorttext",
        "formItemPh number"                  : "shorttext",
    }
    default_image = "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png"
    result = []

    survey = driver.find_elements_by_xpath("//*[starts-with(@id, 'formItem_')]")

    for question in survey:                                                           
        question_id = question.get_attribute("id")
        type_naver = question.get_attribute("class")

        # type
        title = question.find_element_by_xpath(f"//*[@id='{question_id}']/div/div[1]/div[1]/div/span[1]").text

        # body
        body = []
        if type_pocket[type_naver] == "shorttext":
            body = ""
        
        elif type_naver == "formItemPh grid":
                col_selection = []
                col_datas = question.find_elements_by_class_name('gridColHeader')
                row_datas = question.find_elements_by_class_name('gridRowHeader')
                for data in col_datas[1:]:
                    col_selection.append(data.text)
                for data in row_datas:
                    body.append({
                        "title" : data.text,
                        "selection" : col_selection
                    })
        elif type_naver == "formItemPh selectBox":
            select_id= question.find_element_by_xpath("//*[starts-with(@id, 'selectBox_')]").get_attribute("id")
            question_values = question.find_elements_by_xpath(f"//*[@id='{select_id}']/div[2]/div")
            for value in question_values:
                body.append(value.get_attribute("value"))
        else: 
            if type_naver == "formItemPh scale":
                question_values = question.find_elements_by_class_name("optionLabel")
            else:
                question_values = question.find_elements_by_css_selector(f"#{question_id} > div > div.itemOptions.itemOptionPh.displayModeOption.holder.vertical > div > div")
            for value in question_values:
                body.append(value.text)
        
        # main image URL
        try:
            image = (question.find_element_by_xpath(f"//*[@id='{question_id}']/div/div[1]").find_element_by_tag_name("img").get_attribute("src"))
        except:
            image = ""

        # 선택지 이미지
        image_sources = question.find_elements_by_class_name("imageResource")
        image_selections = []
        count = 0
        
        if image:
            image_sources = image_sources[1:]
        for image_source in image_sources:
            if not image_source.get_attribute("src"):
                image_selections.append(default_image)
                count += 1
            else:
                image_selections.append(image_source.get_attribute("src"))
        
        if len(image_sources) == count:
            image_selections = []

        # 필수 여부
        require_mark = question.find_element_by_class_name("requiredMark").get_attribute("style")
        
        if require_mark:
            isrequired = True
        else:
            isrequired = False

        result.append(
            {
                "type": type_pocket[type_naver],
                "title": title,
                "body": body,
                "image_selections": image_selections,
                "url": image,
                "isrequired": isrequired,
            }
        )
    return result

