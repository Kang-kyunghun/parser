
request_data_radio = {
    "surveyId": "779442",
    "urlToken": "rs7mFWc",
    "version": 2,
    "contents" : {
      "survey_title": "모든 타입 설문",
      "survey_description": "모든 타입 설문",
      "googleFormResponseRemoteKey": "엑셀 파일의 s3 remote key",
      "body": [
            {
                "type": "radio",
                "title": "현재 하고 있는 일은?",
                "body": [
                "브랜디",
                "머치스퀘어",
                "리베라비트",
                "위고두팀",
                "기타:"
                ],
                "url": "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/uu/6f00627a-60ca-4d8b-8989-18589e9a6eb1.png",
                "isrequired": True
            }]
        }   
}


request_data = {
    "surveyId": "779442",
    "urlToken": "rs7mFWc",
    "version": 2,
    "contents" : {
      "survey_title": "모든 타입 설문",
      "survey_description": "모든 타입 설문",
      "googleFormResponseRemoteKey": "엑셀 파일의 s3 remote key",
      "body": [
            {
                "type": "shorttext",
                "title": "기수를 입력해주세요",
                "body": "",
                "url": "",
                "isrequired": True,
                "subType": "text",
                
            },
            {
                "type": "radio",
                "title": "현재 하고 있는 일은?",
                "body": [
                "멘토",
                "1차 프로젝트",
                "2차 프로젝트",
                "기업협업",
                "기타:"
                ],
                "url": "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/uu/6f00627a-60ca-4d8b-8989-18589e9a6eb1.png",
                "isrequired": True
            },
            {
                "type": "radio",
                "title": "당신의 나이는?",
                "body": [
                "25",
                "26",
                "27",
                "28",
                "29",
                "30 이상"
                ],
                "url": "",
                "isrequired": True
            },
            {
                "type": "check",
                "title": "해당 하는 것을 선택해주세요 [30대다]",
                "body": [
                "예",
                "아니오",
                "기타:"
                ],
                "url": "",
                "isrequired": True
            },
            {
                "type": "check",
                "title": "해당 하는 것을 선택해주세요 [직장인이다]",
                "body": [
                "예",
                "아니오",
                "기타:"
                ],
                "url": "",
                "isrequired": True
            },
            {
                "type": "check",
                "title": "다녀와본 나라는? (중복 선택 가능)",
                "body": [
                  "영국",
                  "프랑스",
                  "중국",
                  "아이슬란드",
                  "폴란드",
                  "미국",
                  "페루"
                  # "기타:"
                ],
                "url": "",
                "isrequired": True,
                "nid": "Q2",
                "sel_ranges": {
                  "max": 5,
                  "min": 1
                }
              },
            {
                "type": "check_image_selections",
                "title": "현재 기분과 가장 비슷한 것은?",
                "body": [
                  "졸림",
                  "쉬고 싶음",
                  "자신감",
                  "기타:"
                ],
                "url": "",
                "isrequired": False,
                "image_selections": [
                  "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/uu/3b96c893-52f5-4fa2-85f3-97e42e759e09.jpeg",
                  "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/uu/7bca68a9-f2c6-4233-87ea-6ffe0f7c0dd4.jpeg",
                  "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/uu/7bca68a9-f2c6-4233-87ea-6ffe0f7c0dd4.jpeg"

                ],
            },
            
            
            ]
        }   
}


request_data_check = {
    "surveyId": "779442",
    "urlToken": "rs7mFWc",
    "version": 2,
    "contents" : {
        "survey_title": "모든 타입 설문",
        "survey_description": "모든 타입 설문",
        "googleFormResponseRemoteKey": "엑셀 파일의 s3 remote key",
        "body": [
            {
                "type": "check",
                "title": "기술 스택 및 영역은? (중복 선택 가능)",
                "body": [
                  "프론트엔드",
                  "백엔드",
                  "파이썬",
                  "자바스크립트",
                  "장고",
                  "리액트",
                  "노드 js",
                  "기타:"
                ],
                "url": "",
                "isrequired": True,
                "nid": "Q2",
                "sel_ranges": {
                  "max": 5,
                  "min": 1
                }
              }]
        }   
}

request_data_image_select = {
    "surveyId": "779442",
    "urlToken": "rs7mFWc",
    "version": 2,
    "contents" : {
        "survey_title": "모든 타입 설문",
        "survey_description": "모든 타입 설문",
        "googleFormResponseRemoteKey": "엑셀 파일의 s3 remote key",
        "body": [
             {
        "type": "radio_image_selections",
        "title": "이미지 선택",
        "body": [
          "5번으로 갑니다",
          "2"
        ],
        "url": "",
        "isrequired": True,
        "image_selections": [
          "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/uu/3b96c893-52f5-4fa2-85f3-97e42e759e09.jpeg",
          "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/uu/7bca68a9-f2c6-4233-87ea-6ffe0f7c0dd4.jpeg"
        ],
      }]
        }   
}

request_data_shorttext = {
    "surveyId": "779442",
    "urlToken": "rs7mFWc",
    "version": 2,
    "contents" : {
        "survey_title": "모든 타입 설문",
        "survey_description": "모든 타입 설문",
        "googleFormResponseRemoteKey": "엑셀 파일의 s3 remote key",
        "body": [
            {
        "type": "shorttext",
        "title": "주관식 텍스트",
        "body": "",
        "url": "",
        "isrequired": True,
        "subType": "text",
        
      }]
        }   
}
