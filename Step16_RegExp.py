# Step16_RegExp.py

'''
    정규표현식 (Regular Expression) 에 대해서 알아보자
'''

# 어떤 문자열을 검증하거나 혹은 특정 문자열에서 원하는 단어나 기호를 찾아야 될 때가 있다

import re

# 대상 문자열에서
data:str = "apple, banana, cherry"

# "a" 라는 정규표현식에 매칭되는 모든 문자열을 찾아서 LIST에 담아서 리턴
result = re.findall(r"a", data)

# 결과 확인
print(result)


# 대상 문자열2
text:str = "Contact : 010-1111-2222 입니다"

# re.Match 객체를 얻어낸다
m_obj = re.search(r"010-\d{4}-\d{4}", text)  # \d : [0-9]

# 없으면 None, 있으면 re.Match 객체의 참조값
print(m_obj) # re.Match 객체 형태로 출력 // 결과값 : <re.Match object; span=(10, 23), match='010-1111-2222'>
print(m_obj.group()) # .group으로 호출 시, 매치된 문자열이 리턴된다 // 결과값 : 010-1111-2222