import csv
import re
import time
import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def google_form(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(3)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    blueprint = []
    new = []
    body_all = soup.select('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div')
    for i in body_all:
        new.append(i)
    for k in new:
        # 필수 여부
        if k.find('div', {"aria-required": "true"}):
            isrequired = 'true'
        else:
            isrequired = 'false'

        #body
        body = []
        image_selections = []
        default_image = "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png"
        #체크박스
        if k.select("div[role='listitem']"):
            types = 'check'
            for i in k.select("#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div > div > div > div > div > div > label > div > div.docssharedWizToggleLabeledContent"):
                body.append(i.text)
            # image url
            for i in k.select('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div > div > div > div.freebirdFormviewerComponentsQuestionCheckboxRoot > div.freebirdFormviewerComponentsQuestionCheckboxImageCheckboxGroupContainer > div'):
                if i.find('div', {"class": "freebirdSolidBorder freebirdMaterialImageoptionImageWrapper"}):
                    image_selections.append(i.img['src'])
                else:
                    image_selections.append(default_image)    
        
        #라디오
        elif k.select("div[class='freebirdFormviewerComponentsQuestionRadioRoot']"):
            types = 'radio'
            for i in k.select("#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div > div > span > div > div > label > div > div.docssharedWizToggleLabeledContent > div"):
                body.append(i.text)
            #image url            
            for i in k.select('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div > div > span > div > div'):
                if i.find('div', {"class": "freebirdSolidBorder freebirdMaterialImageoptionImageWrapper"}):
                    image_selections.append(i.img['src'])
                else:
                    image_selections.append(default_image)
        
        #드롭다운
        elif k.select("div[role='listbox']"):
            types = 'radio'
            for i in k.select('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div > div > div > div.freebirdFormviewerComponentsQuestionSelectRoot > div > div > div.quantumWizMenuPaperselectOptionList > div > span'):
                body.append(i.text)
        
        #직선단계
        elif k.select("div[role='radiogroup']"):
            types = 'radio'
            for i in k.select('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div > div > div > div.freebirdFormviewerComponentsQuestionScaleRoot > div.appsMaterialWizToggleRadiogroupGroupContainer.exportGroupContainer.freebirdFormviewerComponentsQuestionScaleScaleRadioGroup > span > div > label> div.freebirdMaterialScalecontentLabel'):
                body.append(i.text)

        #단답형 & 장문형 & 날짜 & 시간
        elif k.select("div[class='freebirdFormviewerComponentsQuestionTextRoot']"):
            types = 'shorttext'
        elif k.select("div[class='freebirdFormviewerComponentsQuestionDateDateInputs']"):
            types = 'shorttext'
        elif k.select("div[class='freebirdFormviewerComponentsQuestionTimeTimeInputs']"):
            types = 'shorttext'

        # #title 
        titles = k.findAll('div', {"class" : "freebirdFormviewerComponentsQuestionBaseTitle exportItemTitle freebirdCustomFont"})
        for title in titles:
            title = title.text

            blueprint.append(
                {
                    "type": types,
                    "title": title.rstrip("*"),
                    "body": body,
                    "image_selections": image_selections,
                    "url": "",
                    "isrequired": isrequired,
                }
            )

    return blueprint 

url = "https://forms.gle/i2LwEcXrajvi5YvT8"
print(google_form(url))