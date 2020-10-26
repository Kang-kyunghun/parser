from naver_parser import parsing_naver


def test_form0():
    URL = "http://naver.me/GwaqUXDr"
    assert parsing_naver(URL) == [
        {
            "type": "radio",
            "title": "단일 선택",
            "body": ["옵션 1", "옵션 2", "옵션 3", "옵션 4", "기타 :"],
            "image_selections": [
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=ODEzZjhlZjMtY2E1NC00Y2YwLTgzYzQtZGM0ZjVjNjYxYTYy&filename=6e908041-748f-4196-be76-1ebbd799b110.png",
                "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png",
                "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png",
                "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png",
            ],
            "url": "https://form.office.naver.com/form/getStreamImg.cmd?docId=ODEzZjhlZjMtY2E1NC00Y2YwLTgzYzQtZGM0ZjVjNjYxYTYy&filename=cd867498-8fed-4fc0-afcd-88efd020bffa.png",
            "isrequired": True,
        },
        {
            "type": "radio",
            "title": "단일 선택 (필수x)",
            "body": ["옵션 1", "옵션 2", "옵션 3", "옵션 4"],
            "image_selections": [],
            "url": "",
            "isrequired": False,
        },
        {
            "type": "check",
            "title": "복수 선택",
            "body": ["옵션 1", "옵션 2", "옵션 3", "옵션 4", "옵션 5", "기타 :"],
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "주관식 텍스트(단답)",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "주관식 텍스트",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "주관식 텍스트",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "주관식 텍스트(서술)",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "주관식 텍스트(서술)",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "주관식 텍스트(서술)",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "radio",
            "title": "목록 선택형",
            "body": ['옵션 1', '옵션 2', '옵션 3', '옵션 4'],
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "radio",
            "title": "선호도형",
            "body": ["1", "2", "3", "4", "5"],
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "grid radio",
            "title": "표형",
            "body": [
                {"title": "행 1", "selection": ["열 1", "열 2", "열 3"]},
                {"title": "행2", "selection": ["열 1", "열 2", "열 3"]},
            ],
            "image_selections": [],
            "url": "",
            "isrequired": False,
        },
        {
            "type": "shorttext",
            "title": "이미지 삽입",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "파일",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "날짜 입력",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "날짜/시간 입력",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": False,
        },
        {
            "type": "shorttext",
            "title": "연락처 입력",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "주소 입력",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "금액/숫자 입력",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        },
        {
            "type": "shorttext",
            "title": "",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": False,
        },
    ]


def test_form1():
    URL = "http://naver.me/FVUMm9py"
    assert parsing_naver(URL) == [
        {
            "type": "radio",
            "title": "라디오, main이미지X, 옵션이미지X, 기타X, 필수O",
            "body": ["선택 1", "선택 2", "선택 3", "선택 4"],
            "image_selections": [],
            "url": "",
            "isrequired": True,
        }
    ]


def test_form2():
    URL = "http://naver.me/xxav3Fs8"
    assert parsing_naver(URL) == [
        {
            "type": "radio",
            "title": "라디오, main이미지X, 옵션이미지X, 기타O, 필수X",
            "body": ["선택 1", "선택 2", "선택 3", "선택 4", "기타 :"],
            "image_selections": [],
            "url": "",
            "isrequired": False,
        }
    ]


def test_form3():
    URL = "http://naver.me/IDEv4H5x"
    assert parsing_naver(URL) == [
        {
            "type": "radio",
            "title": "라디오, main이미지O, 옵션이미지X, 기타O, 필수O",
            "body": ["선택 1", "선택 2", "선택 3", "선택 4", "기타 :"],
            "image_selections": [],
            "url": "https://form.office.naver.com/form/getStreamImg.cmd?docId=ZDhjMzIzMzUtMTk5NS00YWU3LThhMTYtMDgxN2M1Y2U0NzVl&filename=196fd3e8-0044-42fa-b87a-b7e0738b34da.png",
            "isrequired": True,
        }
    ]


def test_form4():
    URL = "http://naver.me/5TXr9dp5"
    assert parsing_naver(URL) == [
        {
            "type": "radio",
            "title": "라디오, main이미지X, 옵션이미지(2개), 기타O, 필수O",
            "body": ["선택 1", "선택 2", "선택 3", "선택 4", "기타 :"],
            "image_selections": [
                "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png",
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=ZmJlOTk5MjYtNTM0My00YWIxLTliMDItMjA3MjViYTgyODBi&filename=fb5376a6-8b75-45ec-94cd-c89a52c662b0.jpeg",
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=ZmJlOTk5MjYtNTM0My00YWIxLTliMDItMjA3MjViYTgyODBi&filename=39d965ea-aaba-4e45-9ccc-4e57fa42a58d.jpeg",
                "https://s3.ap-northeast-2.amazonaws.com/pocketsurvey.earlysloth/images/public/blank.png",
            ],
            "url": "",
            "isrequired": True,
        }
    ]


def test_form5():
    URL = "http://naver.me/FA14nyz4"
    assert parsing_naver(URL) == [
        {
            "type": "radio",
            "title": "라디오, main이미지X, 옵션이미지(전부), 기타O, 필수O",
            "body": ["선택 1", "선택 2", "선택 3", "선택 4", "기타 :"],
            "image_selections": [
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=MzIxODEyNmQtYTZjNC00NzcyLWFiYWEtM2EyMDFlN2QyYTkz&filename=8295d786-3f6b-4c59-8195-5fd2fe87f885.jpeg",
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=MzIxODEyNmQtYTZjNC00NzcyLWFiYWEtM2EyMDFlN2QyYTkz&filename=fb5376a6-8b75-45ec-94cd-c89a52c662b0.jpeg",
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=MzIxODEyNmQtYTZjNC00NzcyLWFiYWEtM2EyMDFlN2QyYTkz&filename=39d965ea-aaba-4e45-9ccc-4e57fa42a58d.jpeg",
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=MzIxODEyNmQtYTZjNC00NzcyLWFiYWEtM2EyMDFlN2QyYTkz&filename=622d9121-a35c-4a30-8f7d-07dba28e238a.jpeg",
            ],
            "url": "",
            "isrequired": True,
        }
    ]


def test_form6():
    URL = "http://naver.me/xjNsGXYJ"
    assert parsing_naver(URL) == [
        {
            "type": "radio",
            "title": "라디오, main이미지O, 옵션이미지(전부), 기타O, 필수O",
            "body": ["선택 1", "선택 2", "선택 3", "선택 4", "기타 :"],
            "image_selections": [
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=Njk0YjYyM2MtMjMyYy00Y2JlLWE5MzktODc3ZWYwZmE1ODY3&filename=3a68ea25-0318-4d70-b537-36d5ed03d9f8.jpeg",
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=Njk0YjYyM2MtMjMyYy00Y2JlLWE5MzktODc3ZWYwZmE1ODY3&filename=9f0fefa7-cc7f-4613-ac29-e0930619422d.jpeg",
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=Njk0YjYyM2MtMjMyYy00Y2JlLWE5MzktODc3ZWYwZmE1ODY3&filename=7c968c71-246a-471c-a72a-89ea33e3820b.jpeg",
                "https://form.office.naver.com/form/getStreamImg.cmd?docId=Njk0YjYyM2MtMjMyYy00Y2JlLWE5MzktODc3ZWYwZmE1ODY3&filename=7486d414-dccc-48d5-be98-8e58dea9e461.jpeg",
            ],
            "url": "https://form.office.naver.com/form/getStreamImg.cmd?docId=Njk0YjYyM2MtMjMyYy00Y2JlLWE5MzktODc3ZWYwZmE1ODY3&filename=fb002f0b-440f-4068-a2ae-b795d28eb6fa.png",
            "isrequired": True,
        }
    ]


def test_form7():
    URL = "http://naver.me/x6iHpzv5"
    assert parsing_naver(URL) == [
        {
            "type": "shorttext",
            "title": "shorttext, main이미지X, 필수X, 파일",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": False,
        }
    ]


def test_form8():
    URL = "http://naver.me/xc78iL47"
    assert parsing_naver(URL) == [
        {
            "type": "shorttext",
            "title": "shorttext, main이미지O, 필수O, 파일",
            "body": "",
            "image_selections": [],
            "url": "https://form.office.naver.com/form/getStreamImg.cmd?docId=YjljOWI5YTYtMTUwNy00YTc5LWEzN2EtY2Y3NWVmMTQ0ZWQ3&filename=20c9b687-3e2e-4f88-9676-3ab993ad727b.png",
            "isrequired": True,
        }
    ]

def test_form9():
    URL = "http://naver.me/GyjacfBb"
    assert parsing_naver(URL) == [
        {
            "type": "shorttext",
            "title": "shorttext, main이미지X, 필수O, 이미지",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        }
    ]

def test_form10():
    URL = "http://naver.me/Fn6QJHpL"
    assert parsing_naver(URL) == [
        {
            "type": "shorttext",
            "title": "shorttext, main이미지X, 필수O, 금액/숫자",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        }
    ]

def test_form11():
    URL = "http://naver.me/x8G3bL6O"
    assert parsing_naver(URL) == [
        {
            "type": "shorttext",
            "title": "shorttext, main이미지X, 필수X, 주소",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": False,
        }
    ]

def test_form12():
    URL = "http://naver.me/FOs8BYkR"
    assert parsing_naver(URL) == [
        {
            "type": "shorttext",
            "title": "shorttext, main이미지X, 필수X, 연락처",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": False,
        }
    ]


def test_form13():
    URL = "http://naver.me/x1Xb1Wfh"
    assert parsing_naver(URL) == [
        {
            "type": "shorttext",
            "title": "shorttext, main이미지X, 필수O, 날짜/시간",
            "body": "",
            "image_selections": [],
            "url": "",
            "isrequired": True,
        }
    ]

def test_form14():
    URL = "http://naver.me/x8G3KBVi"
    assert parsing_naver(URL) == [
        {
            "type": "radio",
            "title": "radio, main이미지O, 필수O, 선호도형",
            "body": ["1", "2", "3", "4", "5"],
            "image_selections": [],
            "url": "https://form.office.naver.com/form/getStreamImg.cmd?docId=M2M3MGMzZWYtYmQ4ZS00NzAxLWEzNzYtODQyOWIwNTgyYzQ3&filename=8bcd3381-04dd-4797-ad10-e3bd0bf1e32d.png",
            "isrequired": True,
        }
    ]


def test_form15():
    URL = "http://naver.me/xge6W4A9"
    assert parsing_naver(URL) == [
        {
            "type": "grid radio",
            "title": "grid radio, main이미지O, 필수O, 표형",
            "body": [
                {"title": "12기", "selection": ["1번", "2번", "3번"]},
                {"title": "13기", "selection": ["1번", "2번", "3번"]},
            ],
            "image_selections": [],
            "url": "https://form.office.naver.com/form/getStreamImg.cmd?docId=MWU5ZWQ2MDEtYjhlZC00ZjVhLThlNDYtYmQyZTJlMjQ3ZDg3&filename=74f69084-0e93-439e-bdcd-613235483771.jpeg",
            "isrequired": True,
        }
    ]

def test_form16():
    URL = "http://naver.me/G7ShFUkl"
    assert parsing_naver(URL) == [
        {
            "type": "radio",
            "title": "radio, main이미지O, 필수X, 목록형",
            "body": ['Jack', 'Water', 'May', 'Chans'],
            "image_selections": [],
            "url": "https://form.office.naver.com/form/getStreamImg.cmd?docId=YThjNjc0ZWUtZjhhOS00OTZkLWE2ODgtZTNlNjFmNjJlZWJi&filename=c621bd80-19ca-430f-9263-d6d5d6ef2883.png",
            "isrequired": False,
        },
    ]

def test_form17():
    URL = "http://naver.me/FrLdaGTp"
    assert parsing_naver(URL) == [
        {
            "type": "check",
            "title": "check, main이미지O, 필수X, 복수선택형",
            "body": ['선택 1', '선택 2', '선택 3', '선택 4'],
            "image_selections": [],
            "url": "https://form.office.naver.com/form/getStreamImg.cmd?docId=YzM4OGI5M2MtYWMxZC00YzZmLWJlOWMtZjY0N2FkYjRlNGQ1&filename=5f3af3e8-0000-4bd0-bd89-fe739e2ce5a7.jpeg",
            "isrequired": False,
        },
    ]

