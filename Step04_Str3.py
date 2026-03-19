# yaml 형식의 문자열 다루기

# yaml 문자열을 다룰 때는 외부 모듈을 pip 로 설치를 해서 import 를 해야한다.
# python 가상환경 구성 > pip install
from unittest import result

import yaml

info = '''
name: 신준한
addr: 유성구
foods:
  - 버거
  - 피자
isMan: true
body:
  weight: 75
  height: 175
'''
# yaml 형식의 문자열을 로딩해서 -> dict type으로 변환
result=yaml.safe_load(info)
print("---[1] Dictionary로 변환된 내용---")
print(result)
print(f"Type: {type(result)}")

# dict -> YAML 문자열 변환
# allow_unicode=True: 한글 유니코드 유지
# sort_keys=False: 원래 키 순서 유지 (선택사항)
result2=yaml.dump(result, allow_unicode=True, sort_keys=False)

print("\n---[2] 다시 YAML 문자열로 변환된 내용---")
print(result2)


# 검색 혹인 ai의 도움을 받아서 info 에 들어 있는 문자열을 dict type으로 바꾸기
# 그런 다음 dict에 들어 있는 내용을 확인 후, 다시 dict에 있는 내용을 이용해서 yaml 문자열 형식으로 변환하기

