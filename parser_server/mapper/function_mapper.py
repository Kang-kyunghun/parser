import time
import pandas as pd
from math import isnan
from uuid import uuid4
from .utils import change_time_format


def mapper_radio(data_blueprint, data_answer,  unix_time, uuid):
    answer = data_answer["answer"]
    if str(type(answer)) == "<class 'float'>" :
        answer = ""
    order = data_answer["order"] -1
    body = data_blueprint["contents"]["body"][order]
    selections = body["body"]
    has_etc = False
    is_etc = False
    etc_input = None
    
    if "기타:" in selections:
        has_etc = True
   
    if answer:
        if not data_answer["answer"] in selections:
            is_etc = True
            etc_input = data_answer["answer"]
    
    mapping = {
        
    }
    return mapping

def mapper_radio_image_selections(data_blueprint, data_answer,  unix_time, uuid):
    answer = data_answer["answer"]
    if str(type(answer)) == "<class 'float'>" :
        answer = ""
    order = data_answer["order"] -1
    body = data_blueprint["contents"]["body"][order]
    selections = body["body"]
    image_selections = body["image_selections"]
    has_etc = False
    is_etc = False
    etc_input = None
    
    if "기타:" in selections:
        has_etc = True
        
    if answer :
        if not data_answer["answer"] in selections:
            is_etc = True
            etc_input = data_answer["answer"]
    
    mapping = {
       
    }
    return mapping

def mapper_check(data_blueprint, data_answer,  unix_time, uuid):
    order = data_answer["order"] -1
    body = data_blueprint["contents"]["body"][order]
    selections = body["body"]
    sel_ranges = {"max" : len(selections), "min" : 1}
    has_etc = False
    is_etc = False
    etc_input = None

    if "기타:" in selections:
        has_etc = True

    if str(type(data_answer["answer"])) == "<class 'float'>" :
        answered_text = ''    
    else:
        answers = data_answer["answer"].split(', ')
        etc_answers = []
        
        for answer in answers:
            if not answer in selections:
                etc_answers.append(answer)
        answers = answers[:-len(etc_answers)] if etc_answers else answers
        etc_input = str(etc_answers)[1:-1].replace("'", "") if etc_answers else None
        sel_order = []
        
        if answers:
            for answer in answers:
                sel_order.append(str(selections.index(answer)+1))
        
        if etc_input:
                is_etc = True
                sel_order.append(str(selections.index("기타:")+1))
        
        answered_text = ','.join(sel_order) if not etc_input else ','.join(sel_order) + '|' + etc_input
        
    mapping = {
       
    }
    return mapping

def mapper_check_image_selections(data_blueprint, data_answer,  unix_time, uuid):
    order = data_answer["order"] -1
    body = data_blueprint["contents"]["body"][order]
    selections = body["body"]
    image_selections = body["image_selections"]
    sel_ranges = {"max" : len(selections), "min" : 1}
    has_etc = False
    is_etc = False
    etc_input = None
    
    if "기타:" in selections:
        has_etc = True

    if str(type(data_answer["answer"])) == "<class 'float'>" :
        answered_text = ''    
    else:
        answers = data_answer["answer"].split(', ')
        etc_answers = []
        
        for answer in answers:
            if not answer in selections:
                etc_answers.append(answer)
        answers = answers[:-len(etc_answers)] if etc_answers else answers
        etc_input = str(etc_answers)[1:-1].replace("'", "") if etc_answers else None
        sel_order = []
        
        if answers:
            for answer in answers:
                sel_order.append(str(selections.index(answer)+1))
        
        if etc_input:
                is_etc = True
                sel_order.append(str(selections.index("기타:")+1))
        
        answered_text = ','.join(sel_order) if not etc_input else ','.join(sel_order) + '|' + etc_input
    
    mapping = {
        
    }
    return mapping

def mapper_shorttext(data_blueprint, data_answer,  unix_time, uuid):
    answer = data_answer["answer"]
    if str(type(answer)) == "<class 'float'>" :
        answer = ""
    order = data_answer["order"] -1
    body = data_blueprint["contents"]["body"][order]
    
    mapping = {
        
    }
    return mapping
    