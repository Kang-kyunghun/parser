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
        "formItemPh grid"                    : "radio",
        "formItemPh image"                   : "shorttext",
        "formItemPh file"                    : "shorttext",
        "formItemPh datetime"                : "shorttext",
        "formItemPh phone"                   : "shorttext",
        "formItemPh address"                 : "shorttext",
        "formItemPh number"                  : "shorttext",
    }
    default_image = "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png"
    result = []

    survay = driver.find_elements_by_xpath("//*[starts-with(@id, 'formItem_')]")

    for question in survay:
        question_id = question.get_attribute("id")
        type_naver = question.get_attribute("class")

        # type
        title = question.find_element_by_xpath(f"//*[@id='{question_id}']/div/div[1]/div[1]/div/span[1]").text

        # body
        question_values = question.find_elements_by_css_selector(f"#{question_id} > div > div.itemOptions.itemOptionPh.displayModeOption.holder.vertical > div > div")

        if type_pocket[type_naver] == "shorttext":
            body = ""
        else:
            body = []
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


URL = "http://naver.me/GwaqUXDr"
print(parsing_naver(URL))
