# Step04_Str2.py

'''
    이름과 주소, 좋아하는 음식 2가지를 작성

    [json], xml, [yaml] ... 문자 형식에 맞는 형식

    json은 javascript 객체 표기법을 따르는 문서 형식이다.
    application 이 활용하기에 최적화된 문자열!!
    {
        "key":value, 
        "key2":value2,
            # value가 될 수 있는 타입
            - 숫자 (정수, 실수)
            - "xxx" (문자열은 반드시 더블 따옴표)
            - true / false (논리값)
            - {} : object {"key":value, "key2":value2, ...}
            - [] : array [value, value2, value3, ...]
            - null : 빈 값
        .
        .
    }
'''
# json 형식으로 문자열 작성

#json 모듈 import 하기
import json
from pickletools import read_uint1

# info는 str type이지만 특별한 형식(json)을 띄고 있다
info = '''{
    "name":"신준한",
    "addr":"유성구",
    "foods":["버거","피자"]
}'''

# json의 문자열을 로드(loads)하여, python의 dict type으로 변경함
result = json.loads(info) 
print(result)
print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

# python의 dict type을 덤프(dumps)하여 json의 문자열로 변경함
result2 = json.dumps(result)

print(result2)

print("종료")
