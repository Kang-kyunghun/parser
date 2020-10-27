import pytest
import requests
from bs4 import BeautifulSoup
from crawling import google_form

def test_forms():
    url = "https://forms.gle/esrQ7eX6rBExn4ED8"
    assert google_form(url) == [
        {
            'type': 'check',
            'title': '체크 문항 ',
            'body': ['체크 1', '체크 2'],
            'image_selections': [],
            'url': '',
            'isrequired': 'true',
        },
        {
            'type': 'radio', 
            'title': '드롭다운입니다', 
            'body': ['선택', '옵션1', '옵션2'], 
            'image_selections': [], 
            'url': '', 
            'isrequired': 'false'
        },
        {
            'type': 'shorttext',
            'title': '단답으로 대답해주세요',
            'body': [],
            'image_selections': [],
            'url': '',
            'isrequired': 'false',
        },
        {
            'type': 'shorttext',
            'title': '장문으로 대답해주세요 ',
            'body': [],
            'image_selections': [],
            'url': '',
            'isrequired': 'true',
        },
        {
            'type': 'radio',
            'title': '라디오 선택입니다 ',
            'body': ['라디오 1번', '라디오 2번', '기타:'],
            'image_selections': [],
            'url': '',
            'isrequired': 'true'
        },
        {
            'type': 'radio',
            'title': '직선 질문',
            'body': ['1', '2', '3', '4'],
            'image_selections': [],
            'url': '',
            'isrequired': 'false'
        },
        {
            'type': 'radio',
            'title': '이미지 선택 문항(라디오)',
            'body': ['이미지1', '이미지 없음'],
            'image_selections': ['https://lh4.googleusercontent.com/bEXgw9ePYTjvounCoW_K-gLjmuujWwNY26IEnZqUIXd_OHQXcljgoUHKtBCWgca1Mru-5GN3n3KwbrcXSsyk3oj1ZCLQ7HUSAM0Q5X43UAeVPj0JDW8-FDLjPdnO=w260', 'https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png'],
            'url': '',
            'isrequired': 'false'
        },
        {
            'type': 'check',
            'title': '이미지 선택 문항(체크)',
            'body': ['체크 1', '이미지 선택(체크)', '체크 3'],
            'image_selections': ['https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png', 
'https://lh3.googleusercontent.com/Gd-_NRnICpWxVCoSJ3PbRtqHwQbikMb31oS06k70WPc8NzBsS5Jw253b6QP365Fl3FXF_poppRR7bJXjG9O5ye3culGUPHAAPM9_aHBgQyUZ256ntH1caEUHPDsZ=w260', 
'https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png'],
            'url': '',
            'isrequired': 'false'
        },
        {
            'type': 'check', 
            'title': '이미지 2개(체크)', 
            'body': ['체크선택 1', '체크 선택 이미지1', '체크선택 2', '체크 선택 이미지2', '체크선택 3'], 
            'image_selections': 
['https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png', 
'https://lh3.googleusercontent.com/X1LbcNdmVHfG-UnWG-Ll5uP_29vu6r0mA2W7D86kw59pBiJL_kdrvKjTFXuLqwD_CzIFzy88eDKRUgyU0v8MO8S07gbHCNoLXlrG9Z1XHyDOEjdxquWwfmEW5OYl=w260', 
'https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png', 
'https://lh6.googleusercontent.com/Fw6Sso2dCwtHc8UY2QNR4g7Gs-2mAwSKh0yuvB0QBBFmpcU-ufOKQyi0tSDZ8kVGz-5yRVB1MpbvP0P6pl6n03mj6mOm_gqbQt_b7TLuN6UbkdzK9uMdfoucZY9I=w260', 
'https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png'], 
            'url': '', 
            'isrequired': 'false' 
        },
        {
            'type': 'radio',
            'title': '라디오 두번째',
            'body': ['이미지 선택1', '라디오2', '라디오3'],
            'image_selections': ['https://lh4.googleusercontent.com/k0ff_YsjflRHiDOofj4qnIDzpsrSEyKRH_wZqY6FSgmKpwg2e3TFzjMpfAm07tDrlBMqIZ4fzPX7aOrk8jKZzDPNO9dJywTnm5PbTeAWgR39fN2f0_w9LUqGTNST=w260', 
'https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png', 
'https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png'],
            'url': '',
            'isrequired': 'false'
        },
        {
            'type': 'shorttext',
            'title': '날짜입니다',
            'body': [],
            'image_selections': [],
            'url': '',
            'isrequired': 'false'
        },
        {
            'type': 'shorttext',
            'title': '시간입니다',
            'body': [],
            'image_selections': [],
            'url': '',
            'isrequired': 'false'
        },
    ]


